# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''função que receba uma string s, um caractere x e um número 
    inteiro i entre 0 e o comprimento da string e retorna uma string
    igual s com o elemento da posicao i trocado por x
    entrada:str,str,int
    saida:str'''
    return s[0:i]+x+s[i+1:-1]