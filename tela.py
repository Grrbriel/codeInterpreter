import tkinter as tk
import ttkbootstrap as ttk

import numpy as np                 # v 1.19.2
import matplotlib.pyplot as plt    # v 3.3.2
import matplotlib.patches as patches

import A_lexico as lexi
import A_sintatico as sint

def ImprimeLexicoSintatico():

    inputX = entryString.get()
    lexi.set_input(inputX)
    lexi.tokenizer()
    lexOutput = lexi.get_lexOutput()

    if not lexOutput:
        lexOutput.append("\nNão foi possível analisar o input informado!\n")

    for line in lexOutput:
        txtAnalisLexica.insert("end", "\n" + str(line))

    lexOutput.clear()
    ####################### FIM LEX #######################

    #Gera toda a análise sintática
    sintOutput = sint.sint(inputX)
    if sintOutput is None:
        txtSintatica.insert("end", 'Falha sintática!\n')
    else:
        txtSintatica.insert("end", str(sintOutput)+'\n')

    #MontaPlanoCartesiano()
    PlanoCartesianoMatPlotLib(sintOutput)

def PlanoCartesianoMatPlotLib(sintOutput):

    # Select length of axes and the space between tick labels
    xmin, xmax, ymin, ymax = -10, 10, -10, 10
    ticks_frequency = 1

    # Desenha os pontos
    fig, ax = plt.subplots(figsize=(10, 10))

    # Define escala para o plano
    ax.set(xlim=(xmin - 1, xmax + 1), ylim=(ymin - 1, ymax + 1), aspect='equal')

    # Define a posição 0,0 com centro do plano
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')

    # Remove borda da direita e topo
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Desenha o nome dos eixos x e y(na ponta de cada eixo)
    ax.set_xlabel('x', size=14, labelpad=-24, x=1.03)
    ax.set_ylabel('y', size=14, labelpad=-21, y=1.02, rotation=0)

    # Adiciona mais valores nos eixos x e y(Valores para identificar os pontos)
    x_ticks = np.arange(xmin, xmax + 1, ticks_frequency)
    y_ticks = np.arange(ymin, ymax + 1, ticks_frequency)
    ax.set_xticks(x_ticks[x_ticks != 0])
    ax.set_yticks(y_ticks[y_ticks != 0])

    # Create minor ticks placed at each integer to enable drawing of minor grid
    # lines: note that this has no effect in this example with ticks_frequency=1
    ax.set_xticks(np.arange(xmin, xmax + 1), minor=True)
    ax.set_yticks(np.arange(ymin, ymax + 1), minor=True)

    # Desenha o grid do fundo(quadriculado atrás)
    ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

    # Desenha a seta na pontas dos eixos x e y
    arrow_fmt = dict(markersize=4, color='black', clip_on=False)
    ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
    ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)

    if sintOutput[0] == "circle":
        draw_circle(ax, sintOutput)
    elif sintOutput[0] == "square":
        draw_square(ax, sintOutput)
    elif sintOutput[0] == "rectangle":
        draw_rectangle(ax, sintOutput)
    elif sintOutput[0] == "connect":
        connect_dots(ax,sintOutput)

    plt.show()

def connect_dots(ax,sintOutput):
    xs = []
    ys = []
    for dot in sintOutput:
        if(dot == "connect"):
            print("Conexão de pontos requisitada!\n")
        else:
            xs.append(dot[0])
            ys.append(dot[1])

    ax.scatter(xs, ys)

    for xy in range(len(xs)-1):
        ax.plot([xs[xy], xs[xy+1]], [ys[xy],ys[xy+1]], ls='--', lw=1.5, alpha=0.5)

def draw_rectangle(ax,sintOutput):
    b = patches.Rectangle((sintOutput[2][0], sintOutput[2][1]), sintOutput[1][1], sintOutput[1][0], edgecolor="blue",facecolor="blue", fill=True)
    ax.add_patch(b)
def draw_square(ax,sintOutput):
    a = patches.Rectangle((sintOutput[2][0], sintOutput[2][1]), sintOutput[1], sintOutput[1], edgecolor="blue", facecolor="blue", fill=True)
    ax.add_patch(a)

def draw_circle(ax,sintOutput):
    circulo = plt.Circle((sintOutput[2][0], sintOutput[2][1]), sintOutput[1], facecolor='red', fill=True)
    ax.set_aspect(1)
    ax.add_artist(circulo)


##########################
#--F R M  P R I N C I P A L--
#frm = ttk.Window(themename='darkly')
frm = ttk.Window(themename='journal')
frm.geometry('1000x600')
frm.title("Interpretador")

#--I N P U T--
label = ttk.Label(master=frm, text='Input:', font='Calibri 15')
label.pack()
label.place(x=5, y=10)

input_frame = ttk.Frame(master=frm)
entryString = tk.StringVar()
entry = ttk.Entry(master=input_frame, textvariable=entryString, width=70)
button = ttk.Button(master=input_frame, text='Gerar', command=ImprimeLexicoSintatico)
entry.pack(side='left')
button.pack(side='left', padx=10)
input_frame.pack(pady=10)
input_frame.place(x=5, y=40)

#--L E X I C A  E  S I N T A T I C A--
LayoutAnalises = ttk.Frame(master=frm)
LayoutAnalises.place(width=100)
LayoutAnalises.pack(pady=80)

#--L E X I C A--
LayoutLexica = ttk.Frame(master=LayoutAnalises)
LayoutLexica.pack(side='left', padx=2)

lbl1 = ttk.Label(master=LayoutLexica, text='Análise Léxica:', font='Calibri 10')
lbl1.pack(side='top')

txtAnalisLexica = ttk.Text(master=LayoutLexica)
txtAnalisLexica.place()
txtAnalisLexica.pack(side='left')

#--S I N T A T I C A--
LayoutSintatica = ttk.Frame(master=LayoutAnalises)
LayoutSintatica.pack(side='right')

lbl2 = ttk.Label(master=LayoutSintatica, text='Análise Sintática:', font='Calibri 10')
lbl2.pack(side='top')

txtSintatica = ttk.Text(master=LayoutSintatica)
txtSintatica.place()
txtSintatica.pack(side='right')

frm.mainloop()