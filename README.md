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

---

### 📋 Pré-requisitos e Montagem
**1. Hardware
* Webcam.
* Arduino Uno/Nano conectado via USB. (Para o wokwi foi usado o ESP32 devido a falta)
* Leitor RFID MFRC522
* Tags RFID
* Jumpers







