def freq_palavras(frase):
    """Dada uma string , retorna um dicionário onde cada palavra
    seja chave e tenha como valor o número de vezes que a palavra
    aparece
    str -> dict"""
    chaves = frase.split()
    i=0
    for i in len(chaves):
        valores=list(str(chaves.count(chaves[i])))
        tudo = [chaves,valores]
        i=i+1  
    return dict(tudo)