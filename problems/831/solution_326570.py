def lingua_p(palavra):
    ''' Funcao que recebe uma palavra em portugues e retorna essa mesma
palavra na lingua do p'''
    palavra = palavra.lower()
    NovaPalavra = ''
    vogais = 'aáàâãeéêiíoóôõuú'
    for i in palavra:
        NovaPalavra += 1
        if i in vogais:
            NovaPalavra += 'p' + i
    return NovaPalavra