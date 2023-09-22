def freq_palavras(frases):
    '''funcao que recebera uma string e que retorne um dicionario onde cada palavra dessa string seja uma chave e tenha como valor o numero de vezes que esta palavra aparecera'''
    palavras = frases.split()
    dicionario = {}
    
        for i in palavras:
            contador = palavras.count(i)
            dicionario.update({i: contador})
        return dicionario