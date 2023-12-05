import ply.lex as lex

#Especificação dos tokens
tokens = [
       'NUMBER', #numero inteiro
       'LPAREN', #(
       'RPAREN', #)
       'COMMA',  #,
       'EQUAL',  #=
       'WORDS']   #Palavras reservadas e verificação de violação

reserved = {'connect':'CONNECT', #conectar pontos no plano
             'draw':'DRAW', #desenhar forma especificada
             'square':'SQUARE', #especificar forma
             'triangle':'TRIANGLE', #especificar forma
             'rectangle':'RECTANGLE', #especificar forma
             'size':'SIZE', #especificar tamanho
             'height':'HEIGHT', #especificar altura
             'weight':'WEIGHT', #especificar largura
             'point':'POINT',#especificar ponto no plano
             'AND':'AND', #condicao AND
             'circle':'CIRCLE', #especificar forma
             'start':'START'} #especificar ponto inicial de figura

tokens = tokens + list(reserved.values())

#REGEX DOS TOKENS
t_EQUAL   = r'\='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_COMMA   = r'\,'

#REGEX de palavras e filtragem de palavras reservadas
def t_WORDS(t):
    r'[a-zA-Z]+'
    t.type = reserved.get(t.value)
    if (t.type == None):
        t_error(t)
    else:
        return t

#REGEX de numero inteiro
def t_NUMBER(t):
    #r'\d+'
    r'\-?\d+'
    t.value = int(t.value)
    return t

#REGEX que controla numero de linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#REGEX dos ignorados (espaços e tabulação)
t_ignore  = ' \t'

#REGRA de tratamento de caracter ilegal
def t_error(t):
    print("Illegal character or Word: '%s'" % t.value)
    t.lexer.skip(1)


#BUILD do analisador lexico
lexer = lex.lex()

#String teste simulando input do usuário
input = 'SQUARE connect point(1,1) AND point(2,2) AND point(3,3)\ndraw SQUARE s draw square size = 10 start(4,5)'
input = ''
def set_input(inputX):
    input = inputX
    lexer.input(input)

#INPUT para o analisador
#lexer.input(input)


lexOutput = []
def get_lexOutput():
    return lexOutput


def tokenizer():
    #TOKENIZACAO
    while True: #PRINT (TYPE, VALUE, LINE_NUMBER, POSITION_IN_STRING)
        current_token = lexer.token()
        if not current_token:
            break      #Fim input
        #print(current_token)
        lexOutput.append(current_token)


