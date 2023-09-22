def lingua_p(palavra):
    '''Recebe uma palavra e retorna essa palavra traduzida para a "língua
    do p". Essa tradução consiste em introduzir a letra p e a própria 
    vogal após cada vogal (str -> str)'''
    repeticoes = ''
    for letra in palavra:
        if letra in 'aeiouáàéóôú':
            if letra not in repeticoes:
                palavra = palavra.replace(letra, letra + 'p' + letra)
                repeticoes = repeticoes + letra
    return palavra