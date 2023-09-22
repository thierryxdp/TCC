def freq_palavras(frases):
    '''dada uma frase retorna um dicionario contendo os termos(chaves) presentes na frase e quatas vezes eles se repetem(os valores retornados de cada chave).
string->dict '''
    str.strip(frases)
    total={}
    frases=str.split(frases)
    for palavra in frases:
        if palavra not in total:
            j=list.count(frases,palavra)
            total[palavra]=j
            
    return total