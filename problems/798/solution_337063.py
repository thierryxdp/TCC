# Questão 7 - MT
def freq_palavras(frases):
    '''Calcula a frequência de cada palavra em uma string
    retornando um dicionário com as palavras e suas respectivas frequências
    str --> dict'''

    # dicionário para guardar as palavras e suas frequências
    freq_por_palavra = {}
    # transforma frases numa lista com cada termo sendo uma palavra
    frases = frases.split()

    # itera pela lista frases
    for i in frases:
        # verifica se a palavra em i já está no dicionário
        if i in freq_por_palavra:
            # incrementa em uma unidade a frequência da palavra em i 
            freq_por_palavra[i] += 1
        else:
            # adiciona a palavra em i no dicionário com frequência igual a 1
            freq_por_palavra[i] = 1
    return freq_por_palavra