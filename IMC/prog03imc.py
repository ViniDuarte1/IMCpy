from telnetlib import theNULL
from tkinter import *     # importa framework desktop

janela = Tk()      # cria objeto visual
janela.iconbitmap('D:\Python\IMC\IMC.ico')    # insere favicon

def calculaimc():
    vpeso = float(e_peso.get())
    valtura = float(l_altura())
    imc = vpeso / (valtura * valtura)
    l_resultado['text']=f'{imc:.2f}'

janela.title('Cálculo do IMC') # exibe titulo na barra da janela
janela.geometry('500x500') # define tamanho da janela inicial
janela.configure(bg='white')

frame_cima = Frame(janela, width=500, height=50, bg='#0071B7')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=500, height=300, bg='white')
frame_baixo.grid(row=1, column=0)

app_nome = Label(frame_cima, text='Calculadora do IMC', width=35, height=2,
       bg='#0071B7', fg='white', font='Ivy 16 bold')
app_nome.place(x=0, y=0)

app_linha = Label(frame_cima, width=500, bg='green')
app_linha.place(x=0, y=42)

l_peso = Label(frame_baixo, text='Insira seu peso', height=1, font='Ivy 10 bold', bg='white')
l_peso.place(x=20, y=30)
e_peso = Entry(frame_baixo, width=8)
e_peso.place(x=130, y=30)

l_altura = Label(frame_baixo, text='Insira sua altura', height=1, font='Ivy 10 bold', bg='white')
l_altura.place(x=20, y=60)
e_altura = Entry(frame_baixo, width=8)
e_altura.place(x=130, y=60)

l_resultado = Label(frame_baixo, text='- - -', width=10, height=2, font='Ivy 24 bold',
        padx=6, pady=12, bg='#453DB6', fg='white')
l_resultado.place(x=200, y=10)

l_frase = Label(frame_baixo, text='', width=45, height=1, font='Ivy 12 bold', bg='yellow')
l_frase.place(x=20, y=130)

b_calcular = Button(frame_baixo, text='Calcular', width=45, height=1,
        font='Ivy 12 bold', bg='blue', fg='white', command=calculaimc)
b_calcular.place(x=20, y=200)








janela.mainloop() # ultima linha: fixa a janela na execução.

