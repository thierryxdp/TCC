def freq_palavras(frases):
    """Insere uma string e retorna um dicionário, cada palavra 
    dessa string é uma chave e tem como valor o número de vezes
    que a palavra aparece
    str -> dict"""
    c = 0
    quantas_palavras = {}
    s = str.split(frases)
    for numero in range(len(s)):
        chave = s[c]
        quantas_palavras[chave] = list.count(s, s[c])
        c = c + 1    
    return quantas_palavras
# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis