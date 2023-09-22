def posLetra(frase,letra,numero_de_ocorrencia):
    """funcao que retorna o indice da string que a letra aparece, conforme o numero de ocorrencia colocado;
    str, str, int -> int"""
    i=0
    indice=0
    if numero_de_ocorrencia>str.count(frase,letra):
        return -1
    while str.count(frase,letra,0,i)<numero_de_ocorrencia:
        if str.count(frase,letra,0,i+1)==numero_de_ocorrencia:
            indice=indice+str.index(frase,letra,i)
        i=i+1
    return indice