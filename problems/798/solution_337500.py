def freq_palavras(frases):
    """ Funçao que retorne um dicionario em que cada palavra da string dada
    seja uma chave e tenha como valor o numero de vezes que a 
    palavra aparece"""
    
    frases = str.strip(frases)
    palavras = str.count (frases, ' ') + 1
    dicionario = {}
    dicionario = dict.keys(palavras)
    for i in frases:
        return dicionario