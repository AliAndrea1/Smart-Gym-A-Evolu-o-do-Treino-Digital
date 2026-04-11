import cv2
import time
import mediapipe as mp
import numpy as np
import serial

arduino_conectado = True
try:
    ser = serial.Serial('COM3', 115200, timeout=0.1)
    print("Arduino ON - Sistema pronto!")
except:
    print("Arduino OFF - modo convidado (tecla S)")
    arduino_conectado = False


ALUNOS = {
    "AB:12:CD:34": {"nome": "Aluno", "objetivo": 5}
}

CONVIDADO = {"nome": "Convidado", "objetivo": 5}

estado_app = "AGUARDANDO"
perfil = None

def calcular_angulo(a, b, c):
    a, b, c = np.array(a), np.array(b), np.array(c)

    rad = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    ang = np.abs(rad * 180.0 / np.pi)

    if ang > 180:
        ang = 360 - ang

    return ang


mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
cap = cv2.VideoCapture(0)

contador = 0
estado_mov = None
tempo_rep = time.time()
historico = []

print("Sistema iniciado...")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    tecla = cv2.waitKey(1) & 0xFF


    if estado_app == "AGUARDANDO":

        if arduino_conectado and ser.in_waiting > 0:
            linha = ser.readline().decode().strip()

            if linha in ALUNOS:
                perfil = ALUNOS[linha]
                estado_app = "TREINO"
                contador = 0
                print(f"Bem-vindo {perfil['nome']}")

        if tecla == ord('s'):
            perfil = CONVIDADO
            estado_app = "TREINO"
            contador = 0
            print("Modo convidado")

        cv2.putText(frame, "Aproxime o cartao ou pressione S",
                    (50, h//2), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,255), 2)


    elif estado_app == "TREINO":

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        resultado = pose.process(rgb)

        if resultado.pose_landmarks:
            lm = resultado.pose_landmarks.landmark

            quadril = [int(lm[mp_pose.PoseLandmark.LEFT_HIP].x * w),
                       int(lm[mp_pose.PoseLandmark.LEFT_HIP].y * h)]

            joelho = [int(lm[mp_pose.PoseLandmark.LEFT_KNEE].x * w),
                      int(lm[mp_pose.PoseLandmark.LEFT_KNEE].y * h)]

            tornozelo = [int(lm[mp_pose.PoseLandmark.LEFT_ANKLE].x * w),
                         int(lm[mp_pose.PoseLandmark.LEFT_ANKLE].y * h)]

            angulo = calcular_angulo(quadril, joelho, tornozelo)
            historico.append(angulo)
            if len(historico) > 20:
                historico.pop(0)

            if angulo > 160:
                estado_mov = "em_pe"

            if angulo < 90 and estado_mov == "em_pe":
                estado_mov = "agachado"
                contador += 1

                tempo_atual = time.time()
                duracao = tempo_atual - tempo_rep
                tempo_rep = tempo_atual

                print(f"Agachamento: {contador}")

                if duracao < 1:
                    print("Muito rapido!")

            if angulo > 160:
                cv2.putText(frame, "Desca mais",
                            (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

            if angulo < 70:
                cv2.putText(frame, "Boa profundidade",
                            (50, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

            if len(historico) > 10 and max(historico) < 140:
                cv2.putText(frame, "Fadiga detectada",
                            (50, 140), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,255), 2)

            cv2.putText(frame, f"Angulo: {int(angulo)}",
                        (50, 180), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)

            cv2.putText(frame, f"Reps: {contador}/{perfil['objetivo']}",
                        (50, 220), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,0), 2)

        if contador >= perfil["objetivo"]:
            estado_app = "FINAL"


    elif estado_app == "FINAL":
        cv2.putText(frame, "TREINO FINALIZADO!",
                    (100, h//2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3)

        cv2.imshow("Smart Gym", frame)
        cv2.waitKey(3000)
        estado_app = "AGUARDANDO"

    cv2.imshow("Smart Gym", frame)

    if tecla == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()