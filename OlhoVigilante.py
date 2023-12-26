import cv2
import pyautogui
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pygetwindow as gw
import os  # Importe o módulo os

# Função para minimizar todas as janelas, exceto a barra de tarefas
def minimize_all_windows_except_taskbar():
    for window in gw.getAllTitles():
        if window != "Detecção de Movimento" and window != "Barra de Tarefas":  # Adicione "Barra de Tarefas" como exceção
            gw.getWindowsWithTitle(window)[0].minimize()

# Função para fechar o programa
def close_program():
    root.quit()

# Adicione este código para corrigir o problema da tela preta com PyInstaller
import sys
if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)

# Inicializa o subtrator de fundo MOG2
fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=16, detectShadows=True)

# Inicializa a captura de vídeo da webcam
video_stream = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Cria a janela principal da interface gráfica
root = tk.Tk()
root.title("Detecção de Movimento")

# Cria um botão "Fechar" na interface
close_button = ttk.Button(root, text="Fechar", command=close_program)
close_button.pack()

# Cria um rótulo para exibir o frame da webcam
label = tk.Label(root)
label.pack()

# Função para minimizar todas as janelas quando o movimento é detectado, exceto a barra de tarefas
def minimize_all_programs_except_taskbar():
    minimize_all_windows_except_taskbar()

def update_frame():
    ret, frame = video_stream.read()
    if ret:
        # Aplica o subtrator de fundo no frame
        fgmask = fgbg.apply(frame)

        # Encontra contornos no resultado da subtração de fundo
        contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        movement_detected = False
        for c in contours:
            if cv2.contourArea(c) < 500:  # Altere este valor conforme necessário
                continue

            # Obtém a caixa delimitadora para o contorno
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            movement_detected = True

        # Mostra o frame original e a máscara
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Converte o frame para o formato RGB
        img = Image.fromarray(frame)
        img = ImageTk.PhotoImage(image=img)
        label.img = img
        label.configure(image=img)

        # Minimiza todas as janelas, exceto a barra de tarefas, se movimento for detectado
        if movement_detected:
            minimize_all_programs_except_taskbar()

    # Atualiza a interface gráfica
    root.after(10, update_frame)

# Inicia o loop para atualizar o frame
update_frame()

# Inicia o loop principal da interface gráfica
root.mainloop()

# Limpeza
video_stream.release()
cv2.destroyAllWindows()
