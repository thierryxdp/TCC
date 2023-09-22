# Coloque um comentário dizendo o que a função faz
def freq_palavras(frases):
    '''funcao que dada uma string retorna um dicionario com uma chave pra cada palavra e numero de vezes que ela aparece; str -> dicionario'''
    dicionario = {}
    palavrasSeparadas = str.split(frases)
    for palavra in palavrasSeparadas:
        dicionario[palavra] = dicionario + list.count(palavrasSeparadas, palavra)
        return  dicionario