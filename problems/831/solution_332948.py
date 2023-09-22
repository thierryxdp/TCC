def lingua_p(palavra):
    '''função em que dada uma palavra (em portugues) e retorne esta mesma palavra
    traduzida para a lingua do P; str -> str'''
    vogais=""
    for letra in texto:
        if letra in 'AEIOUaeiou':
            vogais=vogais+letra
    return vogais