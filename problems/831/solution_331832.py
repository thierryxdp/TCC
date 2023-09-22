def lingua_p(palavra):
    '''
    dado um palavra em portugues como argumento, retorna
    a mesma palavra traduzida na linguagem do 
    dado de entrada: str
    retorna: str
    '''
    palavra_traduzida = ''
    for i in palavra:
        if i in 'AEIOUaeiou':
            i = i + 'p' + i
            palavra_trazudida = palavra_traduzida + i
        palavra_traduzida = palavra_traduzida + i
    return palavra_traduzida