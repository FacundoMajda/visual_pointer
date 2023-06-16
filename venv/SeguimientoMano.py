# <----Importamos librerias
import math
import cv2
import mediapipe as mp
import time

# <----- Creamos la clase 'detectormanos'


class detectormanos():
    # <----- Inicializar parametros de deteccion
    def __init__(self, mode=False, maxManos=2, Confdeteccion=0.5, Confsegui=0.5):
        self.mode = mode
        self.maxManos = maxManos
        self.Confdeteccion = Confdeteccion
        self.Confsegui = Confsegui

        # <---- Creacion de objetos para detectar y dibujar mano
        self.mpmanos = mp.solutions.hands
        self.manos = self.mpmanos.Hands(
            self.mode, self.maxManos, self.Confdeteccion, self.Confsegui)
        self.dibujo = mp.solutions.drawing_utils
        # Estos numeros hacen referencia a los nodos de los extremos de los dedos (punta)
        self.tip = [4, 8, 12, 16, 20]

    # <---- Funcion encontrar manos

    def encontrarmanos(self, frame, dibujar=True):
        imgcolor = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.resultados = self.manos.process
        (imgcolor)

        if self.resultados.multi_hand_landmarks:
            for mano in self.resultados.multi_hand_landmarks:
                if dibujar:
                    self.dibujo.draw_landmarks(
                        frame, mano, self.manos.HAND_CONNECTIONS)
        return frame
