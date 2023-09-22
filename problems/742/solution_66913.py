# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """ Função que substitui uma letra de uma string
    na posição indicada pelo inteiro 
    int, int -> str """
    sub = s[:i] +x+ s[1+i:]
    return sub