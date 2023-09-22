def freq_palavras(frases):
    """Recebe uma string e retorna um dicionário onde cada palavra dessa
    string é uma chave e tem como valor o número de vezes que a palavra aparece"""
    vezes_palavra = {}
    lista_frase = str.split(frases)
    for palavra in lista_frase:
        vezes_palavra[palavra] = 1
        if list.count(lista_frase,palavra) >1:
            vezes_palavra[palavra] += list.count(lista_frase,palavra) 
    return vezes_palavra