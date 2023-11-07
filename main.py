import tkinter as tk
import ply.lex as lex
import cProfile

root = tk.Tk()
root.title('Tkinter Window Demo')
root.mainloop()

print ("!")


###ANALISADOR LEXICO
tokens = ['a_par', #(
          'f_par', #)
          'op_vir', #,
          'op_igual', #=
          'op_and', #AND
          'op_eol'] #;

reserverd = {'connect':'connect', #conectar pontos no plano
             'draw':'draw', #desenhar forma especificada
             'square':'square', #especificar forma
             'triangle':'triangle', #especificar forma
             'rectangle':'rectangle', #especificar forma
             'size':'size', #especificar tamanho
             'height':'height', #especificar altura
             'weight':'weight', #especificar largura
             'point':'point'} #especificar ponto no plano
output = []
