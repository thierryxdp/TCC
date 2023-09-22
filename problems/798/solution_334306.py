def freq_palavras(frase):
    """Função que recebe uma string e retorne um dicionário com o
    número de vezes que cada palavra aparece no dicionário: 
    str -> dict"""
    d = dict()
    frase = frase.split()
    
    for c in frase:
        if c not in d:
            d[c] = 1
        else:
            d[c] = d[c] + 1
    return d# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis