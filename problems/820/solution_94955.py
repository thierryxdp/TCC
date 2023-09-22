def posLetra(string,letra,ocorrencia):
    '''Retorna a posição dentro da string
       em que a letra está de acordo com
       a ocorrência inserida;str,str,int->int'''
    contagem=str.index(string,letra)
    indice=0
    while contagem<ocorrencia:
        posicao=indice-1
        indice+=1
        contagem=str.index(string,letra,posicao)
        if contagem>ocorrencia:
            return -1
    return contagem