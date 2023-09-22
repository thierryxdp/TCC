# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """funçao que recebe como parametros uma string s, um caractere x
    e um numero inteiro i, entre 0 e o comprimento da string, e retorna
    uma string igual a s com o elemento da posiçao i trocado pelo 
    caractere x;
    str, int, int -> str
    """
    return s[o:i] + str(x) + s[i+1:]