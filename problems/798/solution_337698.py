def freq_palavras(frases):
    """
    Essa função, dada como argumento uma string qualquer, ela ira 
    retornar  um dicionario em que cada palavra dessa string sera uma chave
    e tera como valor o numero de vezes em que essa palavra aparece 
    na string.
    str->dict
    """
    dicionario = {}
    
    lista_frases = str.split(frases,' ')
    
    for elemento in lista_frases:
        dicionario[elemento] = list.count(lista_frases,elemento)
    return dicionario