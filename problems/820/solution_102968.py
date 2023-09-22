def posLetra(string,letra,numero):
    '''
	função que recebe uma string, uma letra e um número que indica a ocorrencia desejada da letra e retorna em que posição da string aquela ocorrencia está;
    str,str,int->int
    '''
    i = 0
    indice = 0
    if str.count(string,letra) < numero:
        return -1
    while str.count(string,letra) > numero:
        indice = str.find(string,letra,i,len(string))
        i = i + 1
        return i