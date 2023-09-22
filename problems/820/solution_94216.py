def posLetra(string,letra,ocorrencia):
    """Função que recebe uma string, uma letra e um numero que indica a ocorrencia desejada da letra e retorna em que posição da string aquela ocorrencia da letra esta
       Caso exista menos ocorrencias da letra, ela retorna -1
       str,str,int -> int"""
    i=0
    contador=0
    while (contador<ocorrencia and i<len(string)):
        if letra in string[i]:
            contador += 1
            pos = i
        i += 1
    if contador < ocorrencia:
        pos = -1
    return pos