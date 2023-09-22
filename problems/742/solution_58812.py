# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """função que recebe uma string s,um caractere x e um inteiro i entre 0 e o comprimento da string e retorna uma string igual a s,sendo que o elemento da posição i deve ser substituído pelo caractere x"""
    return str(s)[0:int(i)]+str(x)+str(s)[int(i)+1:]