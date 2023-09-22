# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
'''Esta função recebe uma string, e retorna um discionário com uma palavra como
chave seguido de quantas vezes ela repete.
str --> dict
'''
def freq_palavras(frases):
    dic = {}
    total = 0
    frase_tratada = str.split(frases)
    for i in frase_tratada:
        dic[i] = 0
    for i in frase_tratada:
        dic[i] += 1
    return dic