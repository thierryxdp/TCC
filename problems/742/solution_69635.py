# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Funcao que recebe uma string s, um caractere x e um numero inteiro de indice e retorna uma nova string s com o elemento x no lugar do indice indicado;str,str,int-str'''
    s=str (s)
    x=str(x)
    i=int(i)
    s3=s[:i]+x+s[(i+1):]
    return s3