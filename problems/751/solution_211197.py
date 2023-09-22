def quant_palavras(frase):
    ''''A funcao recebe uma frase e retorna a quantidade de palavras dentro da
sentenca str->int'''
    return frase.count(' ',1,len(frase)-1)+1