## Integrantes do grupo:

- Ali Andrea Mamani Molle - 558052
- Guilherme Linard F.R Gozzi - 555768
- Lucas Vasquez Silva - 555159

# Smart Gym: Agachamento com Pose Tracking & RFID

Este projeto integra **Visão Computacional** e **Sistemas Embarcados** para monitorar **agachamentos em tempo real**, identificando usuários via RFID e analisando a execução do exercício com base na biomecânica do movimento.

O sistema utiliza a webcam para rastrear o corpo do usuário e calcula o ângulo do joelho, validando automaticamente as repetições e fornecendo feedback instantâneo.

---

## Funcionalidades
**Identificação Inteligente**
  - Login via RFID (Arduino + MFRC522)
  - Modo convidado pressionando tecla `S`

**Rastreamento Corporal**
  - Detecção de:
    - Quadril
    - Joelho
    - Tornozelo

**Cálculo de Ângulo em Tempo Real**
  - Medição do ângulo do joelho usando trigonometria

**Contagem Automática de Repetições**
  - Em pé → ângulo > 160°
  - Agachado → ângulo < 90°

**Feedback Inteligente**
  -  "Desça mais"
  -  "Boa profundidade"
  -  "Muito rápido!"
  -  "Fadiga detectada"

**Monitoramento**
  - Contador de repetições
  - Meta por usuário
  - Histórico de ângulos

## Pré-requisitos e Montagem
**1. Hardware**
* Webcam.
* Arduino Uno/Nano conectado via USB.
* Leitor RFID MFRC522
* Tags RFID
* Jumpers

### Instalação das Bibliotecas
```bash
pip install opencv-python mediapipe matplotlib pyserial numpy
```
## Configuração e Uso

![Image](https://github.com/user-attachments/assets/4e85af1b-eabf-44a0-83bd-48b3d038d8cf)

**Pinos utilizados:**
- SDA (SS) → Pino 10
- RST → Pino 9

**Funcionamento:**
- O Arduino lê a tag RFID
- Envia o UID via Serial
- O Python identifica o usuário automaticamente

**Como Executar:**
1. Conecte o Arduino na porta COM3
2. Execute o código Python
3. Na tela inicial:
- Aproxime uma tag RFID OU
- Pressione S para modo convidado
4. Posicione-se na frente da câmera
5. Realize o agachamento

**Observações**
O desempenho pode variar com:
- Iluminação
- Posição da câmera
- Visibilidade do corpo





