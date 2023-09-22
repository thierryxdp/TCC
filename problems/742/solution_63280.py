def substitui(s,x,i):
    '''dadas uma string, um caractere x e um número inteiro i entre 0 e o comprimento da string, retorna a string substituindo o caractere na posição i por x 
    str,str,int-->str'''
    return str(s)[0:i]+str(x)+str(s)[i+1:]