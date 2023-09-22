def substitui(s,x,i):
    ''' função que retorna uma string igual a s substituindo a letra na posição i pelo caractere x(s=string,x=caracter,i=número inteiro entre 0 e o comprimento da string)
       string,int,int -> string'''
    frase= str (s)
    nova_frase= str(x) + frase[i:]
    return nova_frase