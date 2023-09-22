def freq_palavras(frases):
    '''função que recebe uma string e retorna um dicionário onde
       cada palavra dessa string seja uma chave e tenha como 
       valor o numero de vezes que a palavra aparece.
       : str -> dict
    '''
    palavras = frases.split()
    dicio = {}
    for palavra in palavras:
        dicio[palavra] = palavras.count(palavra)
    return dicio