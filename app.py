import cv2
import mediapipe as mp
import time
import pygame
import numpy as np
from datetime import datetime

def registrar_evento(tipo):
    with open("eventos_log.txt", "a") as f:
        agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{agora} - ALERTA ATIVADO: {tipo.upper()}\n")

pygame.mixer.init()
pygame.mixer.music.load("alerta.mp3")
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

ultimo_alerta = 0
duracao_alerta = 5  

def tocar_alerta():
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.play()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    brilho_medio = np.mean(gray)

    ambiente_escuro = brilho_medio < 50 
    if ambiente_escuro and time.time() - ultimo_alerta > duracao_alerta:
        tocar_alerta()
        registrar_evento("escuridao")
        ultimo_alerta = time.time()

    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(img_rgb)

    if results.pose_landmarks:
        mp_draw.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        mao_dir = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST]
        ombro_dir = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER]
        mao_esq = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST]
        ombro_esq = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]

        if (mao_dir.y < ombro_dir.y) and (mao_esq.y < ombro_esq.y):
            if time.time() - ultimo_alerta > duracao_alerta:
                tocar_alerta()
                registrar_evento("movimento")
                ultimo_alerta = time.time()

    # Mostra alerta por tempo limitado
    if time.time() - ultimo_alerta <= duracao_alerta:
        cv2.putText(frame, "MOVIMENTO OU ESCURIDAO DETECTADOS!", (0, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    # Mostra brilho na tela (opcional, para testes)
    cv2.putText(frame, f"Brilho: {int(brilho_medio)}", (10, frame.shape[0] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

    # Exibe vídeo
    cv2.imshow("PowerCast Vision", frame)
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
