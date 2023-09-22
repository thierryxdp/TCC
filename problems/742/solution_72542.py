# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função que, recebida uma string s, retorna s porém 
    com o caractere x na posição i, substituindo o elemento
    anterior;
    string, int, int -> string"""
    s = str
    s[i] = str
    stringx = s[0:i] + str(x) + s[x:-1]
    return stringx