def freq_palavras(frase0):
    '''função que dada uma frase retorna um dicionário onde cada palavra é uma chave e tenha como valor
    o número de vezes que a palavra se repete; str->dict'''
    dic={}
    frase1 = str.split(frase0,' ')
    for letra in range(len(frase0)):
        if frase1[letra] in dic:
            dic[frase1[letra]] += 1
        else:
            dic[frase1[letra]] = 1
    return dic