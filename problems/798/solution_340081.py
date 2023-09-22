# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frase):
    '''Dada uma string retona um dicionário que contem o numero de vezes que cada palavra aparece
    str -> dict'''
    dicionario = {}
    s = frase.split()
    for i in range(len(s)):
        dicionario[s[i]] = s.count(s[i])
    return dicionario