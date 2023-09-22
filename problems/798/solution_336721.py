def freq_palavras(frase):
    """Dada uma string , retorna um dicionário onde cada palavra
    seja chave e tenha como valor o número de vezes que a palavra
    aparece
    str -> dict"""
    chaves = frase.split()
    i=0
    while i in range(len(chaves)):
        chaves = list(chaves.count(chaves[i]))
        return chaves