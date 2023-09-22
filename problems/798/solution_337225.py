def freq_palavras(frase):
    '''função que quantas as vezes que uma palavra aparece
    str-->dict'''
    frase= frase.split()
    dicio={}
    for palavra in frase:
        if palavra in dicio:
            dicio[palavra]+=1
        else:
            dicio[palavra]=1
    return dicio