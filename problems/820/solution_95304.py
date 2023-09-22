def posLetra(string,letra,ocorrencia):
    '''Retorna a posição dentro da string
       em que a letra está de acordo com
       a ocorrência inserida;str,str,int->int'''
    count=str.count(string,letra)
    indice=0
    oc=0
    while oc<ocorrencia:
        if letra in string:
            f=str.index(string,letra,ocorrencia)
        oc+=1
        indice+=1    
        if count<ocorrencia:
            return -1
    return f