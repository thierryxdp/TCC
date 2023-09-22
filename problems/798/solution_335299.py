def freq_palavras(texto):
    '''função que recebe como entrada a string "texto" e retorna um dicionário
no qual as chaves são as palavras da string, e o valor dos mapeamentos é o número
de vezes que a palavra aparece no texto; str->dict'''

    final={}
    lista=str.split(texto)

    for x in lista:
        if x not in final:
            final[x]=1
        else:
            final[x]=final[x]+1
    return final