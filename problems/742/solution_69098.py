# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Recebe uma string, numero inteiro e caractere e retorna uma string igual a s, mas com o elemento da posicao i substituido pelo caractere x.
    entrada: str, str, int; saida: str'''
    strP1 = s[0:i]
    strP2 = s[i+1:]
    return strP1 + x + strP2