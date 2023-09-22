def contPalavras(string):
    ''''A funcao recebe uma frase e retorna a quantidade de palavras dentro da
sentenca str->int'''
    return string.count(' ',1,len(string)-1)+1