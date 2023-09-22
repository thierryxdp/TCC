# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Função que recebe uma string s, um caractere x e um número inteiro i entre zero e o comprimento da string e retorna uma string igual a s, mas o elemento da posição i precisa ser substituído por x; string, int, int -> string'''
    fatiamento1= s[0:i]
    fatiamento2=s[i+1:s[len(s)]]
    return fatiamento1 + x + fatiamento2