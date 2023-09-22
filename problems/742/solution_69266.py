# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''funçao que rece uma string s, um caractere x e um numero inteiro x e retorna uma string igual a s. tirando
    que o elemneto da posiçao i foi substituido pelo caractere x.
    str,str,int -> str'''
    mudar= s[:i]+ x + s[i+1:]
    return mudar