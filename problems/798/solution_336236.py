# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frase):
    '''Função que recebe uma str e retorna um dicionário que tenha a str
    como chave e como valor o número de vezes que a palavra aparece'''
    i = 0
    x = str.split(frase)
    dicionario = {}
    for x[i] in x:
        if x[i] in dicionario:
            dicionario[x[i]] += 1 
        else:
            dicionario[x[i]] = 1
    return dicionario