def freq_palavras(frases):
    """ Funçao que retorne um dicionario em que cada palavra da string dada
    seja uma chave e tenha como valor o numero de vezes que a 
    palavra aparece"""
    
    freq_palavras = {}
    frases = str.strip(frases)
    palavras = str.count (frases, ' ') + 1
    for i in frases:
        freq_palavras = dict.keys(frases)
        return freq_palavras