def lingua_p(palavra):
    '''
    Essa função recebe uma palavra e retorna a palavra traduzida para a lingua do p
    
    str -> str
    '''
    palavra_min=str.lower(palavra)
    palavra_p=''
    for x in palavra_min:
        if x in 'aeiou':
            palavra_p=palavra_p+x+'p'+x
        else:
            palavra_p=palavra_p+x
    return palavra_p