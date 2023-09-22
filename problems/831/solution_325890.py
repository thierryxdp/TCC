def lingua_p(palavra):
    ''' função que altera uma palavra em português para a versão
        correspondente na língua do P
        [str--> str]'''

    indice = 0 
    novapalavra = ''

    for letra in palavra:
        if letra not in 'aeiou':
            novapalavra += letra

        if letra in 'aeiou' :
            novapalavra += letra + 'p' + letra
                
    indice += 1

    return str.lower(novapalavra)