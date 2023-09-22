# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''recebe uma string s, um caractere x e um numero 
    	inteiro i entre 0 e o comprimento da string, e 
        retorna uma string igual a s, mas com o caractere
        x no indice i
        str,str,int->str'''
    j=i+1
    return s[0:i]+x+s[j:]