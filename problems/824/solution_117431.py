def posLetra(string,letra,indice):
    '''Recebe como entrada uma string, uma letra
    e um número que indica a ocorrencia desejada da letra
    string,string,int -> int'''
    l_string = string.split()
    i = 0
    tot = 0
    ocorrencia = l_string[indice]
    while i < len(l_string):
        while 'aeiou' not in l_string[i]:
            return(l_strin[i])
    	i += 1