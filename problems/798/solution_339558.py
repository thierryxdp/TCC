def freq_palavras(frases):
    """funcao que recebe uma string e retorna um dicionario onde cada palavra dessa string
    seja uma chave e seu valor seja o numero de vezes que a palavra aparece"""
    dicionario = {}
    palavras = str.split(frases)
    for palavra in palavras:
        cont = list.count(palavras, palavra)
        dicionario[palavra] = cont
        
    return dicionario