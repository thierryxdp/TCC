def lingua_p(palavra):
    '''dada uma palavra, retorna essa palavra traduzida na lingua do p; str -> str'''
    nova_palavra = ''
    for letra in palavra:
        if letra in 'aeiouAEIOU':
            letra = letra + 'p' + letra
            nova_palavra = nova_palavra + letra
        else:
            letra = letra
            nova_palavra = nova_palavra + letra
    return nova_palavra