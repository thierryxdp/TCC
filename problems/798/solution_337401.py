def freq_palavras(frases):
    """ Funçao que retorne um dicionario em que cada palavra da string dada
    seja uma chave e tenha como valor o numero de vezes que a 
    palavra aparece"""
    
    freq_palavras = {}
    for i in str.split(frases):
        frase = str.strip(frases)
        freq_palavras = str.count(frases," ") + 1
        return freq_palavras