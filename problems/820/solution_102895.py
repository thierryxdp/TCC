posLetra(string,letra,indice):
    '''Recebe como entrada uma string, uma letra
    e um número que indica a ocorrencia desejada da letra
    string,string,int -> int'''
   	frase = []
    frase += [string]
    i = 0
    while i < len(frase):
        if letra in frase[i]:
            indice = frase.index(letra)
            return indice