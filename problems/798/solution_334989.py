def freq_palavras (frases):
    """dado uma frase a função  transforma a string em um dicionário 
    onde cada chave é uma palavra e o valor é a quantidadede vezes que aquela palavra apareve na frase
     entrada->str
     retorna ->dict"""
    dicionario={}
    indice=0
    lista_de_palavras= str.split (frases,'')
    
    for i in range (len (lista_de_palavras)):
        if lista_de_palavras[i] not in dicionario:
            dicionario [lista_de_palavras [i]]=1
        if lista_de_palavras [i] in dicionario:
            dicionario [lista_de_palavras [i]]= dicionario [lista_de_palavras [i]]+1
    return dicionario