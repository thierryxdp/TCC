def posLetra(string,letra,num):
    '''Função que recebe uma string, uma letra e um número, que retorna a posiçao da string que a ocorrência da letra está.'''
    '''str,str,int->int'''
    proximo = 0
    ocorrencia = []
    while len(string)>proximo:
        if str.find(string,letra) == -1:
            return -1
        elif string[proximo] == letra:
            ocorrencia = ocorrencia + [proximo]
        proximo = proximo + 1
    if len(ocorrencia)<num:
        return -1
    else:
        return ocorrencia[num -1]