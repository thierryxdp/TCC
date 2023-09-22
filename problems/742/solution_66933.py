# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """função que recebe três elementos:string, caractere e
    um número inteiro entre 0 e o comprimento da string.
    Dada esas informações a função retorna uma string s, exceto
    que o elemneto da posição i deve ser substituido pelo
    caractere x.
    str,str,int -> str"""
    return s[0:i]+x+s[i+1:]