def freq_palavras (frase):
    '''dada uma string retorna um dicionario com o numero de vezes que cada palavra da string aparece'''
    '''str->dici'''
    
    pedaco = str.split (frase)
    resultado = {}
    for palavra in pedaco:
        um = list.count(pedaco, palavra)
        final[palavra] = um
    return resultado