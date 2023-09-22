def posLetra(string,letra,num):
    """Retorna em que posiçao da string a ocorrencia da letra esta, dados:
    uma string, uma letra e um numero que indica a ocorrencia desejada da
    letra(1 para primeira ocorrencia, 2 para a segunda etc...)"""
    
    indice=0
    ocorrencia=0
    
    while indice<len(string):
        if string[indice]==letra:
            ocorrencia+=1
        if ocorrencia==num:
            return string.index(string[indice],indice)
        indice+=1
    else:
         return -1