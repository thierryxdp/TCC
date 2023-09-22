def posLetra(frase,letra,numero):
    """Função que dada uma string, uma letra e um número 
       que indica a ocorrência desejada da letra retorna
       em que posição da string aquela ocorrência da letra
       está (caso exista menos ocorrência de letra do que 
       a ocorrência pedida e função retorna -1).
       str,str,int-> int"""
    posicao = 0
    i = 0
    ocorrencia = 0
    while i < len(frase):
        if letra == frase[i]:
            correncia +=1
        if numero == ocorrencia:
            return posicao 
        i += 1
    else:
        return -1