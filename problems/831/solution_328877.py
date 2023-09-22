def lingua_p(palavra):
    ''' recebe uma palavra e a retorna em lingua do P,
    inserindo a letra p mais a vogal original
    str -> str'''
    lower = str.lower(palavra)
    nova_palavra = ''
    for letra in lower:
        if letra in 'aeiou':
            nova_palavra += letra + 'p' + letra
        else:
            nova_palavra += letra
            
    return nova_palavra