# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''funcao que substitui um caractere na string s de uma determinada posicao
    str, str, int -> str'''
    posicao = i + 1
    parte_1 = s[0:i]
    parte_2 = s[posicao:]
    
    return parte_1 + x + parte_2