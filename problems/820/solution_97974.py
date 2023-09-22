def posLetra(frase,letra,n):
    """Função que receba como entrada uma string, uma letra e um indice e retorna a posição da string dada a letra; str,str,int-> int"""
    x=frase.find(letra)
    while (x>=0 and n>1):
        x=frase.find(letra,x+1)
		n=n-1
    return s