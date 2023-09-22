def freq_palavras(texto):
    ''' dada uma frase retorna um dicionario contendo os termos(chaves) presentes na frase e quatas vezes eles se repetem(os valores retornados de cada chave).
string->dict'''
    total={}
    x=str.split(texto)
    for palavra in x:
        if palavra not in total:
            y=str.count(texto,palavra)
            total+= dict(palavra,y)
    return total