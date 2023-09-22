def lingua_p(palavra):
    '''
    dado uma palavra em portugues como argumento, retorna
    a mesma traduzida na lingua do P
    dados de entrada:str
    retorna: str
    '''
    palavra_traduzida: ''
    for i in palavra:
        if i in 'AEIOUaeiou':
            i = i + 'p' + i
        palavra_traduzida = palavra_traduzida + i
    return str.lower(palavra_traduzida)