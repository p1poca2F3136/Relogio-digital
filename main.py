import tkinter as tk
from tkinter import *
import os
from time import strftime

root = tk.Tk()
root.title('Relógio')
root.geometry("600x320")
root.maxsize(600, 320)
root.minsize(600, 320)
root.configure(background='black')  # Define o fundo da janela como preto

tela = tk.Canvas(root, width=600, height=60, bg='black', bd=0, highlightthickness=0, relief='ridge')
tela.pack()

saudacao = Label(root, bg='black', fg='#8e27ea', font=('Candara', 16))
saudacao.pack()

data = Label(root, bg='black', fg='#8e27ea', font=('Candara', 14))
data.pack(pady=2)

horas = Label(root, bg='black', fg='#8e27ea', font=('Arial', 64, 'bold'))
horas.pack(pady=2)

def get_saudacao():
    nome_usuario = os.getlogin()
    saudacao.config(text='Olá, ' + nome_usuario)

def get_data():
    data_atual = strftime('%a, %d %b %Y')
    data.config(text=data_atual)

def get_horas():
    hora_atual = strftime('%H:%M:%S')
    horas.config(text=hora_atual)
    horas.after(1000, get_horas)  # Chame get_horas() após 1000ms (1 segundo)

get_saudacao()
get_data()
get_horas()

root.mainloop()

#20/10/23