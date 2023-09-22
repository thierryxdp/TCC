def posLetra(frase,letra,n):
    """Função que receba como entrada uma string, uma letra e um indice e retorna a posição da string dada a letra; str,str,int-> int"""
    i=0
    s=0
    while (i<len(frase)):
        x=str.find(frase,letra)
        s= s+ x
        i=i+1
    return s