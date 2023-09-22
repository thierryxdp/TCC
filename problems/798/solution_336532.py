def freq_palavras(frase):
    '''recebe uma string e retorna um diciońario onde cada palavra dessa string seja
uma chave e tenha como valor o ńumero de vezes que a palavra aparece.'''
    separado=str.split(frase)
    dicionario={}
    for palavra in separado:
        if palavra in dicionario:
            dicionario[palavra]+=1
        else:
            dicionario[palavra]=1
    return dicionario