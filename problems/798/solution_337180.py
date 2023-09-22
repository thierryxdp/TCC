def freq_palavras(frases):
    '''Uma funcao que recebe uma string e retorna um dicionario onde cada
    palavra dessa string seja uma chave e tenha como valor o numero de 
    vezes que a palavra aparece
    str -> dici'''
    dicionario={}
    contador = 0
    palavra= ''
    separada = str.split(frases)
    
    for i in separada:
        contador = 0
        for c in separada:
            if c == i:
                contador += 1
        dicionario[i] = contador
    return dicionario