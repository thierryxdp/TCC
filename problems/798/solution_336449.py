def freq_palavras(frases):
    """Função que recebe uma string como chave e retorne um dicionario onde cada palavra seja uma chave e quantas vezes a palavra aparece; str->dict"""
  
	palavras = str.split(frase)
    dicionario = {}
    
    for palavra in palavras:
        if palavra not in dicionario:
            dicionario[palavra]=1
        else:
            dicionario[palavra]=dicionario.get(palavra)+1
    return dicionario