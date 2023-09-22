def posLetra(frase,letra,numero):
    '''Retorna em que posicao da string a ocorrencia da letra esta;
    strin,string,int->int'''
    quant_letras=str.count(frase,letra)
    if quant_letras<numero:
        return -1
    i=0
    ocorrencia=0
    while i<len(frase):
        if frase[i]==letra:
            ocorrencia+=1
        if ocorrencia==numero:
            return i
        i+=1
    return ocorrencia