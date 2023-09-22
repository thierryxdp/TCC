def freq_palavras(frase):
    "função que, dada uma frase, retorna um dicionário onde cada palavra dessa frase seja uma chave e tenha como valor o numero de vezes que a palavra aparece"
    "str -> dicionário"
    lista_palavras=frase.split()
    dicionario={}
    for palavra in lista_palavras:
        numero_palavra=lista_palavras.count(palavra)
        dicionario[palavra]=numero_palavra
    return dicionario