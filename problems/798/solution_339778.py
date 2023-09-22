def freq_palavras(frases):
    '''Função que recebe uma string e retorna um dicionário em que em que cada palavra da string seja uma chave e tenha como valor o número de vezes de aparição da palavra'''
    palavras = frases.split()
    dicionario = {}
    
    for i in palavras:
        contador = palavras.count(i)
        dicionario.update({i: contador})
        return dicionario