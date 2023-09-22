# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''função que retorna uma string igual a s, 
    com o elemento de posição i substituído por x.
    entrada: string, int, int
    saída: string'''
    if (0<=i<= len(s)):
        return s[0:i] + s[i+1:len(s)]