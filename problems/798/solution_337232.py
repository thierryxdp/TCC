def freq_palavras(frase):
    '''Função recebe frase e retorna com a quantidade de vez 
    que cada palavra aparece. str-->dict'''
    palavras = frase.split()
    dicionario = {}
    i = 0
    for elementos in palavras:
        dicionario[palavras[i]]=palavras.count(palavras[i])
        i+=1
        return dicionario