def substitui(s,x,i):
    'dados uma string,um caractere e um numero retorne uma string igual a s exceto que na posição i esteja x. str,str,int-->str'
    str[i]=x
    return str[0:i] + x + str[i+1:]