# Função que retorna dicionário encontrado e número de ocorrências
def freq_palavras(frases):
    # str --> dic
    palavras = frases.split()
    dicionario = {}
    for i in palavras:
        if i not in dicionario:
            dicionario[i]=palavras.count(i)
    return dicionario