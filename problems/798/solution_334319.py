def freq_palavras(frases):
    '''Recebe uma frase e retorna um dicionário 
    que contém a palavra e a quantidade de 
    vezes que ela aparece
    str->dict'''
    frases=frases.split()
    dicio={}
    for palavra in frases:
        dicio[palavra]=list.count(frases,palavra)
    return dicio