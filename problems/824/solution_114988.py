def uppCons(frase):
    """A Entrada é a frase que está no parâmetro e o retorno
    será essa frase com as letras consoantes em maiúsculo e as
    vogais e demais caracteres permanecerão comona frase
    original"""
    #str -> str
    variavel = 0
    consoantes = 'bcdfghjklmnpqrstvwxz'
    while variavel < len(consoantes):
        fraseA = frase.replace(consoantes.upper)
    fraseA = fraseA + 1
    return fraseA