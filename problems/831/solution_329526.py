def lingua_p(palavra):
    '''recebe uma palavra e retorna essa mesma palavra adicionando apos
    cada vogal a sequencia de letras 'p' + a vogal original; a funcao ignora
    a diferenca entre letras maiusculas e minusculas, retornando a palavra traduzida
    toda em minuscula'''
    palavra2 = ''
    for letra in palavra:
        if letra in 'aeiou':
            palavra2 += letra+'p'+letra
        else:
            palavra2 += letra
    return palavra2