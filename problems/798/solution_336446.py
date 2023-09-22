def freq_palavras(frases):
    """Retorna um dicionário em que cada palavra da string dada
    como entrada é uma chave e o número de vezes que a palavra
    aparece é o valor associado
    str -> dict"""
    d = {}
    for i in str.split(frases):
        if i in d:
            d[i]+=1
        else: 
            d[i]=1
    return d