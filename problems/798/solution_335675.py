def freq_palavras(frase):
    ''' dada uma frase retorna um dicionario contendo os termos(chaves) presentes na frase e quatas vezes eles se repetem(os valores retornados de cada chave).
string->dict'''
    total={}
    x= str.split(frase)
    for palavra in	x:
        if palavra not in total:
            y=str.count(frase,palavra)
            total+=dict(palavra,y)
            return total