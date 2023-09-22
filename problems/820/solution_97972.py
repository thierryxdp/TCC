def posLetra(frase,letra,n):
    """Função que receba como entrada uma string, uma letra e um indice e retorna a posição da string dada a letra; str,str,int-> int"""
    x=str.find(frase)
    while (x>=0 and n>1):
        x=str.find(frase,x+1)
		n=n-1
    return s