def posLetra(frase,letra,n):
    """essa funcao retorna em que posição da string a letra esta dados como parâmetros uma string, a letra e um inteiro que indica a ocorrencia desejada da letra, se tiver menos ocorrencia da letra que a pedida a função retorna -1
    str,int->str"""
    posicao=0
    proximo=str.find(frase,letra,n)
    while proximo < len(frase):
        if str.count(frase,letra)<=n:
            return -1
        elif str.count(frase,letra)>=n:
            posicao= str.find(frase,letra,(n-(str.find(frase,letra,proximo))))
        proximo = proximo +1
    return posicao