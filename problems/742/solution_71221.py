# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função que recebe a string s, um caractere x e um 
    número inteiro i entre 0 e o comprimento da string, e
    retorna uma string igual a s, porém com o elemento da 
    posição i substituído pelo caractere x"""
    return str(s)[:i]+"x"+str(s)[i+1:]