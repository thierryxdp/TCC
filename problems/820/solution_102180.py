def posLetra(string,letra,n):
    '''funçao que calcula e retorna a posiçao da string que a ocorrencia esta. str,str,int->int'''
    proximo = 0
    ocorrencia = []
    while len(string)>proximo:
        if str.find(string,letra) == -1:
            return -1
        elif string[proximo] == letra:
            ocorrencia = ocorrencia + [proximo]
        proximo = proximo + 1
    if len(ocorrencia)<n:
        return -1
    else:
        return ocorrencia[n -1]