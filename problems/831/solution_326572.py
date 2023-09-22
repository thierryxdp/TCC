def lingua_p(palavra):
    ''' Funcao que recebe uma palavra em portugues e retorna essa mesma
palavra na lingua do p'''
    palavra = palavra.lower()
    NovaPalavra = ''
    vogais = 'aáàâãeéêiíoóôõuú'
    for i in palavra:
        NovaPalavra += i
        if i in vogais:
            NovaPalavra = NovaPalavra + 'p' + i
    return NovaPalavra