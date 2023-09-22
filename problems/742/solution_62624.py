# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Essa função recebe uma string s, um caractere x e um número inteiro
    i entre 0 e o comprimento da string e retorna uma string igual a s
    trocando o elemento da posição i por x. str||int||int,str"""
    if 0<=i <= len(s):
        return str.replace(s,s[i],x)