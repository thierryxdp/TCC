def posLetra(string,letra,numero):
    '''
	função que recebe uma string, uma letra e um número que indica a ocorrencia desejada da letra e retorna em que posição da string aquela ocorrencia está;
    str,str,int->int
    '''
    indice = 0
    if str.count(string,letra) < numero:
        return -1
    elif str.count(string,letra) > numero:
        while indice < numero:
            indice = str.index(string,letra,indice,len(string)) + 1
        return indice
    else:
        return str.index(string,letra)