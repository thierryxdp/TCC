def lingua_p(palavra):
    '''Recebe uma palavra e retorna essa palavra traduzida para a "língua
    do p". Essa tradução consiste em introduzir a letra p e a própria 
    vogal após cada vogal (str -> str)'''
    letras = palavra.split()
    for letra in letras:
        if letra in 'aeiou':
            palavra = palavra.replace(letra, letra + 'p' + letra)
    return palavra