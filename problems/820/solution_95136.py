def Letra(string,letra,ocorrencia):
    '''Retorna a posição dentro da string
       em que a letra está de acordo com
       a ocorrência inserida;str,str,int->int'''
    indice=0
    ocorrenciaDaVez=0
    while ocorrenciaDaVez<ocorrencia:
        if string[indice]==letra:
            indice+=1
    return indice