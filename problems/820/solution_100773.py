def posLetra(string,letra,ocorrencia):
    '''dada uma string, retorna o indice da n ocorrencia
    de uma letra nessa string
    str,str,int->int'''
    cont=0
    indice=0
    if letra not in string:
        return -1
    while cont<ocorrencia:
        if string[indice]==letra:
            cont=cont+1
        indice=indice+1
    return indice-1