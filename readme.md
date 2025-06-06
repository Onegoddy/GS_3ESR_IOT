```markdown
```
# PowerCast Vision - Detecção de Falta de Energia com IA

---

## :movie_camera: Vídeo de demonstração
* https://youtu.be/JmDAU5d6SSM

---

## :warning: Descrição do problema

Durante uma queda de energia, ambientes como **hospitais, residências de idosos, creches e centros de dados** ficam altamente vulneráveis. A ausência de iluminação pode levar a **acidentes**, como quedas, confusões ou movimentos de risco.  
Além disso, identificar e reagir rapidamente a essas situações de emergência é um desafio — principalmente sem sensores físicos ou sistemas especializados.

---

## :bulb: Visão geral da solução

O **PowerCast Vision** é uma solução desenvolvida com **Python e MediaPipe**, que **detecta movimentos humanos suspeitos** (como levantar os dois braços pedindo ajuda) e **identifica ambientes escuros** por meio de visão computacional.  
Quando uma dessas situações é detectada, o sistema:

- 🔊 Emite um alerta sonoro
- 🖼️ Exibe uma imagem de aviso na tela
- 📝 Registra o evento em um log com **data, hora e tipo de alerta**

### 🧪 Tecnologias utilizadas:
- `MediaPipe` para detecção de gestos e poses humanas
- `OpenCV` para captura de vídeo e análise de brilho
- `Pygame` para reprodução de som
- `NumPy` para cálculos de brilho
- `Datetime` para registro em log

---

## :gear: Instruções de uso

1. Instale o [Anaconda](https://www.anaconda.com/download) (recomendado).
2. Crie e ative um ambiente virtual:
   ```bash
   conda create -n powercast python=3.9
   conda activate powercast
   ```
3. Instale as dependências:
   ```bash
   pip install opencv-python mediapipe pygame numpy
   ```
4. Coloque os arquivos `alerta.mp3` e (opcional) `alerta_visual.png` na mesma pasta do script.
5. Execute o arquivo `powercast_vision.py` com o ambiente ativado.

---

## :file_folder: Código Fonte

> Todo o código está disponível neste repositório, no arquivo principal:

- `powercast_vision.py` – script que executa o sistema completo
- `eventos_log.txt` – arquivo de log que será criado automaticamente ao rodar o sistema
- `alerta.mp3` – som tocado ao detectar risco
- `alerta_visual.png` (opcional) – imagem exibida no alerta

---

## 👥 Integrantes

- João Pedro Marques Rodrigues – RM98307  
- Kayky Paschoal Ribeiro – RM99929  
- Natan Eguchi dos Santos – RM98720
```

