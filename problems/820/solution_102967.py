posLetra(string,letra,indice):
    '''Recebe como entrada uma string, uma letra
    e um número que indica a ocorrencia desejada da letra
    string,string,int -> int'''
    while i < len(string):
        if letra in frase[i]:
            indice = frase.index(letra)
            return indice