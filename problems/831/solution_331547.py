def lingua_p(palavra):
    '''Recebe como uma palavra e retorna esta mesma palavra traduzida para a lingua do P;
    string -> string'''
    
    nova_palavra = ''

    for letra in palavra:
        if letra in 'aeiouáéíú':
            nova_palavra += letra + 'p' + letra
        else:
            nova_palavra += letra

    return nova_palavra