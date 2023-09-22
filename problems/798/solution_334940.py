def freq_palavras(frase):
    '''funcao que, dada uma frase, retorna o numero de vezes que cada palavra aparece na
    frase;
    str -> dict(str,int)'''
    lista=str.split(frase)
    ocorrencias={}
    for palavra in lista:
        ocorrencias[palavra]=str.count(frase,palavra)
    return ocorrencias