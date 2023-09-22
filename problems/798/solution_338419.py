def freq_palavras(frases):
    '''função que recebe uma string e retorna
    um dicionário em que cada palavra dessa
    string seja uma chave e tenha como valor
    correspondente o número de vezes que a 
    palavra aparece
    str -> dicionario'''
    palavras = frases.split()
    dicionario = {}
    
    for i in palavras :
        contador = palavras.count(i)
        dicionario.update({i:contador})
    return dicionario