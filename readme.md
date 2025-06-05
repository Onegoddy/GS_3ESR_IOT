```markdown
```
# PowerCast Vision - Detecção com Alerta

## :movie_camera: Demonstração
* https://youtu.be/JmDAU5d6SSM

---

## :memo: Descrição do projeto

O **PowerCast Vision** é um sistema de visão computacional que utiliza a biblioteca **MediaPipe** para detectar movimentos humanos (levantamento dos braços) e monitora a **luminosidade ambiente** via webcam. Quando é detectado um ambiente escuro ou uma movimentação específica (ambos os braços levantados), o sistema **aciona um alerta sonoro**, exibe uma **mensagem de aviso na tela**, e **registra o evento em um arquivo de log** com data, hora e tipo de alerta.

---

## :books: Funcionalidades

- 🎯 **Detecção de movimento humano** (levantamento dos dois braços).
- 🌑 **Monitoramento de luminosidade** com base no brilho médio da imagem.
- 🔊 **Alerta sonoro automático** quando o ambiente estiver escuro ou quando o usuário levantar os dois braços.
- 🖼️ **Mensagem de alerta visual** e sobreposição de imagem na tela da câmera.
- 📊 **Exibição do nível de brilho atual** (útil para debug e testes).
- 📝 **Geração de log de eventos** em `eventos_log.txt` com data, hora e motivo do alerta.

---

## :seedling: Instruções de uso

1. Instale o **[Anaconda](https://www.anaconda.com/download)** (caso ainda não tenha).
2. Abra o **Anaconda Prompt (`cmd.exe`)**.
3. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   conda create -n powercast python=3.9
   conda activate powercast
   ```
4. Instale as dependências:
   ```bash
   pip install opencv-python mediapipe pygame numpy
   ```
5. Certifique-se de que:
   - O arquivo de som `alerta.mp3` esteja na mesma pasta do script.
   - (Opcional) Uma imagem PNG com transparência chamada `alerta_visual.png` esteja na pasta para exibição no alerta.
6. Abra o **Visual Studio Code pelo Anaconda Navigator** ou via terminal com:
   ```bash
   code .
   ```
7. Execute o script Python no Visual Studio Code com o ambiente ativado.

---

## :clipboard: Requisitos

- Anaconda com Python 3.7+
- Webcam funcional
- Arquivo de som `alerta.mp3`
- (Opcional) Arquivo `alerta_visual.png` para visualização gráfica no alerta
- Sistema operacional compatível com `pygame` (Windows recomendado)

---

## :hammer: Dependências

- `opencv-python`: Captura e processamento de vídeo.
- `mediapipe`: Detecção de poses humanas.
- `pygame`: Reprodução de som de alerta.
- `numpy`: Cálculo de brilho da imagem.
- `datetime`: Registro de hora dos eventos.

---

## :wrench: Tecnologias utilizadas

- Python
- OpenCV
- MediaPipe
- Pygame
- NumPy
- Anaconda
- Visual Studio Code

---

## :handshake: Colaboradores

- João Pedro Marques Rodrigues - RM98307  
- Kayky Paschoal Ribeiro - RM99929  
- Natan Eguchi dos Santos - RM98720
```
