def posLetra(string,letra,ocorrencia):
    '''Retorna a posição dentro da string
       em que a letra está de acordo com
       a ocorrência inserida;str,str,int->int'''
    contagem=str.index(string,letra)
    indice=0
    c=str.index(string,letra,ocorrencia)
    while contagem<ocorrencia:
        posicao=indice-1
        indice+=1
        contagem=str.index(string,letra,posicao)
        if c>ocorrencia:
            return -1
    return contagem