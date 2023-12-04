import tkinter as tk
import ttkbootstrap as ttk
import cartesianPlane
import pygame

import numpy as np                 # v 1.19.2
import matplotlib.pyplot as plt    # v 3.3.2
import matplotlib.patches as patches

def ImprimeLexicoSintatico():
    txtAnalisLexica.insert("end", 'TESTE AQUI 1 \nTESTE AQUI 1')
    txtSintatica.insert("end", 'TESTE AQUI 2 \nTESTE AQUI 2')

    #MontaPlanoCartesiano()
    PlanoCartesianoMatPlotLib()

def MontaPlanoCartesiano():
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)

    # Set up the window
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Plano Cartesiano')

    plane = cartesianPlane.CartesianPlane(screen)
    #plane.zooming(10000)
    #plane.scale(100)

    circle = cartesianPlane.Circle(plane, RED, (0, 0), 10)
    rect = cartesianPlane.Rect(plane, GREEN, [20, 10, 10, 10])
    line = cartesianPlane.Line(plane, BLUE, [40, 0], [10, 10])
    path = cartesianPlane.Path(plane, YELLOW, [0, 0], [10, 10], [20, 20])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

            plane.event_handling(event)

        # Update the plane
        plane.update()

        cartesianPlane.draw.circle(plane, GREEN, (15, 15), 1)
        cartesianPlane.draw.rect(plane, BLUE, (25, 25, 10, 10), 1)
        cartesianPlane.draw.line(plane, YELLOW, (35, 35), (45, 45))

        #clock.tick()

        # Update the screen
        pygame.display.update()

def PlanoCartesianoMatPlotLib():


    # Select length of axes and the space between tick labels
    xmin, xmax, ymin, ymax = -5, 5, -5, 5
    ticks_frequency = 1

    # Desenha os pontos
    fig, ax = plt.subplots(figsize=(10, 10))

    # Defini escala para o plano
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

    # --R E T A--
    # Definindo como Vetor os pontos
    xs = [0, 2, -3, -1.5]
    ys = [0, 3, 1, -2.5]
    colors = ['m', 'g', 'r', 'b']
    ax.scatter(xs, ys, c=colors)
    # LigarPontosComlinha
    ax.plot([0, 2], [0, 3])
    # Desenha a linha pontilha que conecta os pontos ao eixo
    #for x, y, c in zip(xs, ys, colors):
    #    ax.plot([x, x], [0, y], c=c, ls='--', lw=1.5, alpha=0.5)
    #    ax.plot([0, x], [y, y], c=c, ls='--', lw=1.5, alpha=0.5)

    #--C I R C U L O--
    #https://acervolima.com/como-desenhar-um-circulo-usando-matplotlib-em-python/
    #PrimeiraForma
    #theta = np.arange(1, 2*np.pi, 0.01)
    #r = np.sqrt(4)
    #x = r*np.cos(theta)
    #y = r * np.sin(theta)
    #plt.plot(x,y)
    #SegundaForma
    #circulo = plt.Circle((1, 1), 2)
    #ax.set_aspect(1)
    #ax.add_artist(circulo)

    #--R E T A N G U L O--
    #https://www.delftstack.com/pt/howto/matplotlib/how-to-draw-rectangle-on-image-in-matplotlib/
    #a = patches.Rectangle((1, 1), 1, 2, edgecolor="blue", facecolor="blue", fill=True)
    #ax.add_patch(a)

    plt.show()

#--F R M  P R I N C I P A L--
#frm = ttk.Window(themename='darkly')
frm = ttk.Window(themename='journal')
frm.geometry('1000x600')
frm.title("Janela")

#--I N P U T--
label = ttk.Label(master=frm, text='Enunciado:', font='Calibri 15')
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