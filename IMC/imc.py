from cProfile import label
from tkinter import *

janela = Tk()      # cria objeto visual
janela.iconbitmap('D:\Python\IMC\IMC.ico')    # insere favicon
janela.title("IMC")
janela.geometry('300x300')
janela.configure(bg='#7FFFD4') # cor da janela

def calculaimc():
    vpeso = float(peso.get())
    valtura = float(altura.get())
    imc = vpeso / (valtura * valtura)
    l_resultado['text']=f'{imc:.2f}'
    
    if(imc < 18,5):
        l_frase['text']='palito'
    if(imc >= 18,5 and imc < 25):
        l_frase['text']='brabo'
    if(imc >= 25 and imc < 30):
        l_frase['text']='saliente'
    if(imc >= 30 ):
        l_frase['text']='bola'

        
        
        
    
# muda cor de uma parte em cima
frame_cima = Frame(janela, width=300,height=50, bg='#008080')
frame_cima.grid(row=0,column=0)
#mesma coisa ai de cima oh muda a cor pra ver
frame_baixo = Frame(janela, width=300,height=250, bg='#7FFFD4')
frame_baixo.grid(row=1,column=0)

app_name = Label(frame_cima,text="CALCULADORA DE IMC", width=25, height=2, bg='#008080', fg='black', font='times')
app_name.place(x=0,y=0)


f_peso = Label(frame_baixo,text="Digite seu peso:  ")
f_peso.place(x=0,y=0)
peso = Entry(frame_baixo, width=20) # como se fosse input, recebe o valor da variavel
peso.place(x=95,y=0) # informa local da frase

f_altura = Label(frame_baixo,text="Digite sua altura: ") # exibe a frase
f_altura.place(x=0,y=20) 
altura = Entry(frame_baixo, width=20)
altura.place(x=95,y=20)

l_resultado = Label(frame_baixo, text='- - -', width=5, height=1, font='Ivy 24 bold',
        padx=6, pady=12, bg='#453DB6', fg='white')
l_resultado.place(x=100, y=100)

l_frase = Label(frame_baixo, text='', width=20, height=1, font='Ivy 12 bold', bg='yellow')
l_frase.place(x=50, y=170)

#button
bcalcular = Button(frame_baixo,  text="CALCULAR", command=calculaimc)
# posição do button
bcalcular.place(x=115,y=50)



# fixa a janela
janela.mainloop()