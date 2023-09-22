def posLetra(string,letra,ocorrencia):
    """Função que recebe uma string, uma letra e um numero que indica a ocorrencia desejada da letra e retorna em que posição da string aquela ocorrencia da letra esta
       Caso exista menos ocorrencias da letra, ela retorna -1
       str,str,int -> int"""
    x=0
    contador=0
    while x<len(string) and contador<ocorrencia:
        if string[x]==letra:
            contador = contador + 1
            x = x + 1
    if contador<ocorrencia:
        return "foram encontradas" + str(contador) + "ocorrencias de" + str(letra)
    else:
        return i-1