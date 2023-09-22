def freq_palavras(frases):
    '''funcao que recebe uma string e retorna um dicionário em que 
    cada palavra da string seja uma chave e tenha como valor o numero
    de vezes de aparicao da palavra'''
    palavras = frases.split()
    dicionario = {}
    
    for i in palavras:
        contador = palavras.count(i)
        dicionario.update({i: contador})
    return dicionario