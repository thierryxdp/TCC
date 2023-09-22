def lingua_p(palavra: str) -> str:
    """ recebe uma palavra, e retorna ela traduzida para
    a 'linguagem P' """
    
    vogais = 'abcde'
    palavra1 = ''
    
    for i in palavra:
        if i in 'aeiouáéíóú':
            palavra1 += i + 'p' + i
        else:
            palavra1 += i
            
    return palavra1