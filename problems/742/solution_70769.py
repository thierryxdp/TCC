# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
        '''Função que retorna uma string igual a s, 
exceto que o elemento da posição i deve ser substituído
por x, dadas as entradas s(string), x(inteiro) e i( de
0 até comprimento da string)
str, ,int -> str'''
    s[i]=x
    return s