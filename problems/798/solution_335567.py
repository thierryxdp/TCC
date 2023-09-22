def freq_palavras(frases):
    """funcao que recebe de entrada uma string e retorna
    um dicionario onde cada palavra dessa string e uma chave
    e tem como valor o numero de vezes que a palavra aparece;
    str -> dict"""
    
    lista = [0]
    espacos = 0
    while espacos < len(frases):
        if frase[espacos] = '':
            lista = lista + espacos
        espaco = espacos + 1
    elemento = 1
    dicionario = {}
    while elemento < len(lista):
        palavra = frases[lista[elemento - 1],lista[elemento]]
        numero = str.count(frases,palavra)
        dicionario = dicionario + palavra:numero
        elemento = elemento + 1
    return dicionario + frases[lista[-1]:]:str.count(frases,frases[lista[-1]:])