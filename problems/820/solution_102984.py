def posLetra(string,letra,indice):
    '''Recebe como entrada uma string, uma letra
    e um número que indica a ocorrencia desejada da letra
    string,string,int -> int'''
    l_string = string.split()
    i = 0
    tot = 0
    ocorrencia = l_string[indice]
    while i < len(l_string):
        if letra in l_string[0][i]:
            tot += 1
        return tot

    	i += 1