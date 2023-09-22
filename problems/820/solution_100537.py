def posLetra(frase,letra,ocorrencias):
    """Função que recebe uma frase, uma letra e um determinado número de
    ocorrências dessa letra. A função retorna o índice no qual a frase alcança o
    número de ocorrências desejado para aquela letra
    str,str,int->int"""
    registradas=0
    indice=0
    total=str.count(frase,letra)
    if total<ocorrencias:
        return -1
    while registradas<ocorrencias and indice<len(frase):
        if frase[indice]==letra:
            registradas=registradas+1
        indice=indice+1
    return indice-1