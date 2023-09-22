def lingua_p(palavra):
    '''Dado uma palavra em portugues, retorna esta mesma palavra traduzida para lingua do P.
    Onde apos cada vogal é inserida uma letra p mais a vogal da palavra original.
    str -> str'''
    cont=0
    palavraseparada=list(palavra)
    for i in palavra:
        if i in 'AEIOUaeiouéáúó':
            palavraseparada[cont]=i+'p'+i
        cont=cont+1
    return str.join('',palavraseparada)