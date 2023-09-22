def freq_palavras(frases):
    """Função que recebe uma string e retorna um dicionário
    onde cada palavra da string seja uma chave e tenha como
    valor o número de vezes que a palavra aparece.
    str->dict"""
    quant=0
    dicionario={}
    a=frases.split()
    for i in range(len(a)):
        quant=list.count(a,a[i])
        dicionario[a[i]]=quant
    return dicionario