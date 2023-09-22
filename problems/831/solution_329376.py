def lingua_p(palavra):
    '''retona a palavra traduzida para a língua P'''
    '''str -> str'''
    
    min = str.lower(palavra)
    vogal = 'aeiouáéíú'
    final= ''
    
    for letra in min:
        if letra in vogal:
            final += letra + 'p' + letra
        else:
            final = final + letra
            
    return final