reversed ={
    'Elements' : 'TELEMENTS',
    'element' : 'TELEMENT',
    'type' : 'TTYPE',
    'item' : 'TITEM',
    'Carnet' : 'TCARNET',
    'DPI' : 'TDPI',
    'Nombre' : 'TNOMBRE',
    'Carrera' : 'TCARRERA',
    'Password' : 'TPASSWORD',
    'Creditos' : 'TCREDITOS',
    'Edad' : 'TEDAD',
    'Correo' : 'TCORREO',
    'Descripcion' : 'TDESCRIPCION',
    'Materia' : 'TMATERA',
    'Fecha' : 'TFECHA',
    'Hora' : 'THORA',
    'Estado' : 'TESTADO',
}


tokens=[
    'LQUESTION','RQUESTION','DOLAR','ID','IGUAL','NUMERO','NORMSTRING'
]+ list(reversed.values())

t_LQUESTION = r'\¿'
t_RQUESTION = r'\?'
t_DOLAR = r'\$'
t_IGUAL = r'\='

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reversed.get(t.value,'ID')
    return t

def t_NUMERO(t):
    r'\d+'
    try:
        t.value= int(t.value)
    except ValueError:
        print("Error en %d ",t.value)
        t.value=0
    return t

def t_NORMSTRING(t):
    r'\".*?\"'
    t.value = t.value[1:-1] # remuevo las comillas
    #print("la cadena es: ", t.value)
    return t    

# Ignored characters
t_ignore = ' \t\r\n'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print(f"Illegal character {t.value[0]!r}")
    t.lexer.skip(1)

import ply.lex as lex
import re
lexer = lex.lex(reflags=re.IGNORECASE)