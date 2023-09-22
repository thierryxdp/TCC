def posLetra(string,letra,numero):
    """Recebe uma string, uma letra e uma numero, e retorna em que posição
    da string a ocorrencia determinada pelo numero está.
    str,str,int -> int
    """
    i = 0
    contagem = 0
    if string.count(letra)>=numero:
        while contagem != numero:
            if letra == string[i]:
                contagem+=1
            i = i + 1
        return i - 1
    else:
        return -1