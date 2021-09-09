from Analizadores.Lexico import tokens
from ..Estudiantes import Estudiante
from ..Tareas import Tareas
#diccionario de nombres
names = {}

def p_statement_group(t):
    'statement : LQUESTION TELEMENTS RQUESTION elementos LQUESTION DOLAR TELEMENTS RQUESTION'
    print('Ok')

def p_elementos_group(t):
    """elementos : elementos elemento
                 | elemento    
                 """
    
def p_elemento(t):
    'elemento : LQUESTION TELEMENT tipoElemento RQUESTION items LQUESTION DOLAR TELEMENT RQUESTION'


def p_tipoElemento(t):
    """tipoElemento : TTYPE IGUAL NORMSTRING
    """

def p_items(t):
    """items : items item
             | item
             """

def p_item(t):
    """item : LQUESTION TITEM tipoItem IGUAL valorItem DOLAR RQUESTION
    """

def p_valorItem(t):
    """valorItem : NORMSTRING
                 | NUMERO
                 """
    
def p_tipoItem(t):
    """tipoItem : TCARNET
                | TDPI
                | TNOMBRE
                | TCARRERA
                | TPASSWORD
                | TCREDITOS
                | TEDAD
                | TCORREO
                | TDESCRIPCION
                | TMATERA
                | TFECHA
                | THORA
                | TESTADO
                | ID
                """
    

def p_error(t):
    print("Error sintactico '%s'" % t.value)
    
import ply.yacc as yacc
parser=yacc.yacc()