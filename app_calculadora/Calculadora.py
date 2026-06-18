from tkinter import *
from math import log, sqrt
import os
import sys

def caminho_recurso(nome_arquivo):
    if getattr(sys, "frozen", False):
        # Executando como .exe
        return os.path.join(sys._MEIPASS, nome_arquivo)
    # Executando como .py
    return os.path.join(os.path.dirname(__file__), nome_arquivo)


#Cores da calculadora
dict_colors={
    'gray':'#808080',
    'blue_gray':'#a7c9d1',
    'white': '#FFFFFF',
    'orange': '#FFA500',
    'grizzly':'#eceff1'
}
#Código da calculadora:
app=Tk()
app.title('CALCULADORA')
app.geometry('355x365')
app.resizable(False, False)
app.config(bg=dict_colors['gray'])

#Criação do cabeçalho
app.title("calculadora")
app.iconbitmap(caminho_recurso("icoane.ico"))

#Criação de frame:
frame_tela= Frame(app,width=357,height=60)
frame_tela.grid(row=0,column=0)
frame_corpo= Frame(width=357,height=70,bg=dict_colors['gray'])
frame_corpo.grid(row=1,column=0)

armazem_valores=''

#Função de entrada...
def entrada_dado(event):
    global armazem_valores
    armazem_valores=armazem_valores+str(event)
    valor_texto.set(armazem_valores)

#Função de calculo:

def calculo():
    try:

        global armazem_valores
        expressao = []
        for i in armazem_valores:
            if i == '^':
                expressao.append('**')
            elif i == '√':
                expressao.append('sqrt')
            elif i == 'log':
                expressao.append('log(')
            else:
                expressao.append(i)

        expressao_final = ''.join(expressao)
        resultado = eval(expressao_final)
        armazem_valores=str(resultado)
        valor_texto.set(resultado)


    except Exception as erro:
        print(erro)
        valor_texto.set('Error')

#Função limpar tela
def limpar_tela():
    global armazem_valores
    armazem_valores=''
    valor_texto.set('0')

#Apagador de digito
def apagador_digito():
    global  armazem_valores
    armazem_valores=armazem_valores[:-1]
    valor_texto.set(armazem_valores)

#Visor da calculadora
valor_texto = StringVar()
valor_texto.set("0")
app_label = Label(frame_tela,textvariable=valor_texto,width=21,height=2,padx=7,relief="flat",anchor='e',justify="right",font=('Arial', 18, 'bold'),bg=dict_colors['blue_gray'])
app_label.grid(row=0, column=0)

#Crição botões:
#Limpar
bt_c=Button(app,command= limpar_tela, text='AC',width='8',height='3',bg=dict_colors['orange'])
bt_c.place(x=5,y=65)
#Conchete da direta:
bt_cld=Button(app,command=lambda:entrada_dado('('),text='(',width='8',height='3',bg=dict_colors['orange'])
bt_cld.place(x=75,y=65)
#Conchete da esquerda:
bt_cle=Button(app,command=lambda:entrada_dado(')'),text=')',width='8',height='3',bg=dict_colors['orange'])
bt_cle.place(x=145,y=65)
#Calculo da divisão e retornando o resto:
bt_31=Button(app,command=lambda:entrada_dado('%'),text='%',width='8',height='3',bg=dict_colors['orange'])
bt_31.place(x=5,y=245)
#Calculo de exponenciação
bt_31=Button(app,command=lambda:entrada_dado('^'),text='X^Y',width='8',height='3',bg=dict_colors['orange'])
bt_31.place(x=5,y=305)
#Calculo de logaritmo
bt_31=Button(app,command=lambda:entrada_dado('log('), text='log X',width='8',height='3',bg=dict_colors['orange'])
bt_31.place(x=75,y=305)
#apagar o digito anterior
bt_31=Button(app,command=apagador_digito, text='⌫',width='8',height='3',bg=dict_colors['orange'])
bt_31.place(x=215,y=65)
#Botão da raiz
bt_11=Button(app,command=lambda:entrada_dado('√('), text='√X',width='8',height='3',bg=dict_colors['orange'])
bt_11.place(x=5,y=125)
#Botão da divisão e retorno de um número inteiro
bt_21=Button(app,command=lambda:entrada_dado('//'), text='//',width='8',height='3',bg=dict_colors['orange'])
bt_21.place(x=5,y=185)
#Igualdade
bt_i=Button(app, command=calculo,text='=',width='18',height='3',bg=dict_colors['orange'])
bt_i.place(x=215,y=305)
#Operações básicas
bt_a=Button(app,command=lambda:entrada_dado('+'),text='+',width='8',height='3',bg=dict_colors['orange'])
bt_a.place(x=285,y=65)
bt_s=Button(app,command=lambda:entrada_dado('-'), text='-',width='8',height='3',bg=dict_colors['orange'])
bt_s.place(x=285,y=125)
bt_d=Button(app, command=lambda:entrada_dado('/'),text='/',width='8',height='3',bg=dict_colors['orange'])
bt_d.place(x=285,y=185)
bt_m = Button(app,command=lambda:entrada_dado('*'), text='x', width='8', height='3',bg=dict_colors['orange'])
bt_m.place(x=285,y=245)
# Numeros /coluna2
bt_12=Button(app,command=lambda:entrada_dado('1'), text='1',width='8',height='3')
bt_12.place(x=75,y=125)
bt_22=Button(app,command=lambda:entrada_dado('4'), text='4',width='8',height='3')
bt_22.place(x=75,y=185)
bt_32=Button(app,command=lambda:entrada_dado('7'), text='7',width='8',height='3')
bt_32.place(x=75,y=245)
#Numeros/coluna3
bt_13=Button(app,command=lambda:entrada_dado('2'), text='2',width='8',height='3')
bt_13.place(x=145,y=125)
bt_23=Button(app,command=lambda:entrada_dado('5'), text='5',width='8',height='3')
bt_23.place(x=145,y=185)
bt_33=Button(app,command=lambda:entrada_dado('8'), text='8',width='8',height='3')
bt_33.place(x=145,y=245)
#Numero/coluna4
bt_14=Button(app,command=lambda:entrada_dado('3'), text='3',width='8',height='3')
bt_14.place(x=215,y=125)
bt_24=Button(app,command=lambda:entrada_dado('6'), text='6',width='8',height='3')
bt_24.place(x=215,y=185)
bt_34=Button(app,command=lambda:entrada_dado('9'), text='9',width='8',height='3')
bt_34.place(x=215,y=245)
#Numero/linha5
bt_34=Button(app,command=lambda:entrada_dado('0'), text='0',width='8',height='3')
bt_34.place(x=145,y=305)

'''
from tkinter import *: Importa todas as funções e classes do módulo básico Tkinter.

from tkinter import ttk: Importa o módulo de "temas" do Tkinter.

abertura=Tk(): Cria a janela principal da sua aplicação (a "raiz" ou root).

.title('CALCULADORA'): Define o texto que aparecerá na barra de título.
abertura.mainloop(): Inicia o loop de eventos. 

.geometry(): É o método utilizado para configurar o tamanho. 
 
'''
app.mainloop()

import os
print(os.getcwd())