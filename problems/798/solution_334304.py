# 
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frase):
    """Função que recebe uma string e retorne um dicionário com o
    nuúmero de vezes quecada palavra aparece 
    str -> dict"""
    d = dict()
    for c in frase:
        if c not in d:
            d[c] = 1
        else:
            d[c] = d[c] + 1
    return d