def lingua_p(palavra):
    '''funcao dada uma palavra retorna a palavra com um p depois de cada vogal e repete a vogal.
    str -> str'''
    palavra_p = ''

    for letra in palavra:

        if letra in 'aeiou':

            palavra_p = palavra_p+letra+'p'+letra

        else:

            palavra_p = palavra_p+letra

    return palavra_p