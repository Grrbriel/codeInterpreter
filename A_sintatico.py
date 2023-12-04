# Yacc example

import ply.yacc as yacc
from A_lexico import tokens

def p_draw(p):
    '''
    draw : DRAW SQUARE
        | DRAW SQUARE SIZE EQUAL NUMBER
        | DRAW SQUARE START LPAREN NUMBER COMMA NUMBER RPAREN
        | DRAW SQUARE START LPAREN NUMBER COMMA NUMBER RPAREN AND SIZE EQUAL NUMBER
        | DRAW CIRCLE
        | DRAW CIRCLE SIZE EQUAL NUMBER
        | DRAW CIRCLE START LPAREN NUMBER COMMA NUMBER RPAREN
        | DRAW CIRCLE START LPAREN NUMBER COMMA NUMBER RPAREN AND SIZE EQUAL NUMBER
        | DRAW RECTANGLE
        | DRAW RECTANGLE HEIGHT EQUAL NUMBER AND WEIGHT EQUAL NUMBER
        | DRAW RECTANGLE START LPAREN NUMBER COMMA NUMBER RPAREN
        | DRAW RECTANGLE START LPAREN NUMBER COMMA NUMBER RPAREN AND HEIGHT EQUAL NUMBER AND WEIGHT EQUAL NUMBER
    '''
    if p[2] == "square":
        p[0] = p_SQUARE(p)

    elif p[2] == "circle":
        p[0] = p_CIRCLE(p)

def p_SQUARE(p): #Padrão para o front: [FORMA, INT TAMANHO / TUPLA HEIGHT-WEIGHT, TUPLA START]
    '''
    square : SQUARE
    '''
    if len(p.slice) == 6: #quadrado com tamanho
        p[0] = [p[2], p[5], (0, 0)]

    elif len(p.slice) == 9: #quadrado com start point
        p[0] = [p[2], 5, (p[5], p[7])]

    elif len(p.slice) == 13: #quadrado com start point e tamanho
        p[0] = [p[2], p[12], (p[5], p[7])]

    else: #quadrado padrão
        p[0] = ['square', 5, (0, 0)]

    return p[0]

def p_CIRCLE(p):
    '''
    circle : CIRCLE
    '''
    if len(p.slice) == 6: #circulo com tamanho
        p[0] = [p[2], p[5], (0, 0)]

    elif len(p.slice) == 9: #circulo com start point
        p[0] = [p[2], 5, (p[5], p[7])]

    elif len(p.slice) == 13: #circulo com start point e tamanho
        p[0] = [p[2], p[12], (p[5], p[7])]

    else: #circulo padrão
        p[0] = ['circle', 5, (0, 0)]

    return p[0]
def raw_input(p):
    pass

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()

def sint(inputX):
    #while True:
    try:
        #s = input('exp: ')
        s = inputX
    except EOFError:
        print("FIM")
    result = parser.parse(s)
    print(result)

    return result

