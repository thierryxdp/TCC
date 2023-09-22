# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
import string as st
def substitui(s,x,i):
    ''' entra com uma lista s e substitui a componente i pelo elemento x'''
    lista = s[0:i]+str(x)
    return lista