# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    ''' Retorna a quantidade de palavras de uma dada frase
    str -> dict'''
    lista_frases = frases.split(' ')
    dicionario = {}
    
    for i in range(len(lista_frases)):
        if lista_frases[i] in dicionario:
        	dicionario[lista_frases[i]] += 1
        else:
            dicionario[lista_frases[i]] = 1
    return dicionario