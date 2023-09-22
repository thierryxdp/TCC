def freq_palavras(x):
    """Essa função serve para contar o número de vezes que uma palavra se repete
    em uma frase
    str->dict"""
    lista_palavras = x.split()
    dic = dict.fromkeys(lista_palavras,0)
    for i in range(len(lista_palavras)):
        dic[lista_palavras[i]] += 1
    return dic

#freq_palavras("Opa, boa tarde!") == {'Opa,': 1, 'boa': 1, 'tarde!': 1}
#freq_palavras("o que é o que é ?") == {'o': 2, 'que': 2, 'é': 2, '?': 1}
#freq_palavras("Há pessoas que amam o poder, e outras que têm o poder de amar") == {'Há': 1, 'pessoas': 1, 'que': 2, 'amam': 1, 'o': 2, 'poder,': 1, 'e': 1, 'outras': 1, 'têm': 1, 'poder': 1, 'de': 1, 'amar': 1}