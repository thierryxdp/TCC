# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    ''' Dado s - string, x - caractere, i - entre o coprimento da string, \n
    retorna a string s trocando o simbolo x na posição i.
    entrada: s,x,i -> str, int, int 
    saida: str '''
    x = str (x)
    if i >= 0:
        return s[0:i]+x+s[(i+1):]