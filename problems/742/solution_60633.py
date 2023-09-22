def substitui(s,x,i):
    """Função que recebe uma palavra, um carcter e um número inteiro, ela transforma a palavra em 
    uma lista, depois define outra variável que recebe o caracter a ser acrescido a lista substituindo na posição do 
    número inteiro. A função retorna uma string parecida com a enserida na entrada, porém, o com um caracter alterado"""
    lista= list(s)
    letra= x
    lista[i] = letra
    return ''.join(lista)