def posLetra(string,letra,num):
    '''
        Funcao recebe uma string, uma letra que pertence a
        string dada e um numero que indica a ocorrencia desejada
        da letra na string, e retorna em que posicao a ocorrencia
        da letra está.
        str, str, int -> int
        
    '''
    ocorrencias = 0

    if num <= string.count(letra):
        while ocorrencias < (num - 1):
            string = string.replace(string[string.find(letra)],' ',1)
            ocorrencias = ocorrencias + 1
        return string.find(letra)
    else:
        return -1