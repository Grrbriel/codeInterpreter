import ply.yacc as yacc
from A_lexico import tokens

def p_draw_conn(p):
    '''
    draw_conn : DRAW SQUARE
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
        | CONNECT conn AND conn
        | CONNECT conn AND conn AND conn
        | CONNECT conn AND conn AND conn AND conn
        | CONNECT conn AND conn AND conn AND conn AND conn
        | CONNECT conn AND conn AND conn AND conn AND conn AND conn
        | CONNECT conn AND conn AND conn AND conn AND conn AND conn AND conn
        | CONNECT conn AND conn AND conn AND conn AND conn AND conn AND conn AND conn
        | CONNECT conn AND conn AND conn AND conn AND conn AND conn AND conn AND conn AND conn
        | CONNECT conn AND conn AND conn AND conn AND conn AND conn AND conn AND conn AND conn AND conn
    '''

    if p[1] == "connect":
        for x in range(len(p.slice)):
            if type(p[x]) == list:
                if(p[0] is None):
                    p[0] = p[x]
                else:
                    p[0] = p[0] + p[x]
        p[0] = ["connect"]+p[0]

    elif p[2] == "square":
        p[0] = p_SQUARE(p)

    elif p[2] == "circle":
        p[0] = p_CIRCLE(p)

    elif p[2] == "rectangle":
        p[0] = p_RECTANGLE(p)

def p_conn(p):
    '''
    conn : POINT LPAREN NUMBER COMMA NUMBER RPAREN
    '''
    x = [[p[3], p[5]]]
    p[0] = x



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

def p_RECTANGLE(p):
    '''
    rect : RECTANGLE
    '''
    if len(p.slice) == 10: #retangulo com tamanho
        p[0] = [p[2], (p[5], p[9]), (0, 0)]

    elif len(p.slice) == 9: #retangulo com start point
        p[0] = [p[2], (2, 5), (p[5], p[7])]

    elif len(p.slice) == 17: #retangulo com start point e tamanho
        p[0] = [p[2], (p[12], p[16]), (p[5], p[7])]

    else: #retangulo padrão
        p[0] = ['rectangle', (2, 5), (0, 0)]

    return p[0]
def raw_input(p):
    pass

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
    error = True



# Build the parser
parser = yacc.yacc()

error = False

def sint(inputX):
    #while True:
    try:
        #s = input('exp: ')
        s = inputX
    except EOFError:
        print("FIM")
    result = parser.parse(s)
    print(result)
    if error is False:
        return result
    else:
        return "Erro sintático no input!!!"

