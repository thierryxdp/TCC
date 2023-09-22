def lingua_p(palavra):
    '''fun ̧cao que recebe palavra em portugues e
retorna palavra traduzida em lıngua do p.
str--> str'''
    traduzido_p = []
    contador = 0
    for letra in list(palavra):
        if letra in 'aeiou ́a ́e ́ı ́o ́u1:
            traduzido_p.append(letra + 'p' + letra)
        
        else:
            traduzido_p.append(letra)
            
    return ' '.join(traduzido_p)