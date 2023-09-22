def freq_palavras(frase):
    """Função que recebe uma string e retorna um dicionario com a palavra dessa string contenha o valor
de quantas vezes a palavra aparece. str->dic"""
    
    palavras = str.split(frase)
    dicionario = {}
    
    for palavra in palavras:
        if palavra not in dicionario:
            dicionario[palavra]=1
        else:
            dicionario[palavra]=dicionario.get(palavra)+1
    return dicionario