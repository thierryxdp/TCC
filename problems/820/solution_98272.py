def posLetra(frase,letra,numero):
    """Função que dada uma string, uma letra e um número 
       que indica a ocorrência desejada da letra retorna
       em que posição da string aquela ocorrência da letra
       está (caso exista menos ocorrência de letra do que 
       a ocorrência pedida e função retorna -1).
       str,str,int-> int"""
    posicao = 0
    i = 0
    while i < len(frase):
        if str.count(frase,letra) <= numero :
            posicao = str.find(frase,letra,posicao)
            i +=1
        return posicao
    else:
        return -1