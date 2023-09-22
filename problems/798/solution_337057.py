def conta_palavras(frase):
    """Dipões o número de vezes que cada
    palavra aparece numa string em uma lista.
    string -> list
    """
    lista_palavras = str.split(frase," ")
    lista_contagem = []
    i=0
    while i<len(lista_palavras):
        list.append(lista_contagem,list.count(lista_palavras,lista_palavras[i]))
        i=i+1
    return lista_contagem

def dicio(frase):
    """Cria um dicionário que relaciona as palavras de uma frase
    (as chaves), com o número de vezes que ela aparece nessa string,
    (os valores).
    string -> dict
    """
    lista_palavras = str.split(frase," ")
    dicio={}
    i=0
    for palavra in str.split(frase," "):
        dicio[lista_palavras[i]] = conta_palavras(frase)[i]
        i=i+1
    return dicio