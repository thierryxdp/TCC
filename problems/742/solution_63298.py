'''função que, a partir de uma string, um caractere e um número inteiro, retorna uma string em que o caractere que ocupava a posição do número inteiro na string original é subistituido pelo novo caractere no dado de entrada'''
#(s)= string original, (x)= novo caractere (i)= número inteiro 
# string,string,int-> string
def substitui(s,x,i):
    str(s)[i]= str(x)
    return str(s)