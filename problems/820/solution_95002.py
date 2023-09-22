def posLetra(string,letra,ocorrencia):
    '''Retorna a posição dentro da string
       em que a letra está de acordo com
       a ocorrência inserida;str,str,int->int'''
    contagem=str.count(string,letra)
    indice=0
    tamanho=len(string)-1
    while tamanho<ocorrencia:
        index=str.index(string,letra,contagem)
    indice+=1 
    return contagem