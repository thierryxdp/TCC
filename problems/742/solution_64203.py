def substitui (s,x,i):
    """ recebe uma string, um caractere e um numero inteiro como parametro. retorna a string com o caractere no lugar ocupado pelo numero inteiro (i deve ir de 0 - comprimento da string);
    str,str,int->str"""
    metade1=s[0:i]
    metade2=s[i+1:]
    return metade1+x+metade2