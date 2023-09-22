def conta_palavra (palavra, frase):
    '''retorna quanta vezes uma palavra se repete numa frase
    str ->int''' 
    
    lista = str.split (frase)
    contador = 0
    for element in lista :
        if palavra == element:
            contador += 1
    return contador

def freq_palavras (frase):
    '''função que dada uma frase retorna um dicionário com as palavras da frase e o
    valor dela é a quantidade de vezes que ela se repete na frase
    str -> dict'''
    
    lista =str.split (frase)
    dicionario = {}
    
    for palavra in lista:
        dicionario [palavra] = conta_palavra (palavra, frase)
        
    return dicionario