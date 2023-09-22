def freq_palavras(frases):
    '''função recebe string e retorna dicionario com quantidade
    de cada palavra dessa string;
    str => dict'''
    
    palavra= frases.split()
    dicionario = {}
    qtd = 0
    for i in palavra:
        dicionario[palavra[qtd]] = palavra.count(palavra[qtd])
        qtd = qtd+1
    return dicionario