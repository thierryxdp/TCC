# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    lista = frases.split(' ')
    dic = dict()
    for palavra in lista:
        dic[palavra] = lista.count(palavra)
    return dic