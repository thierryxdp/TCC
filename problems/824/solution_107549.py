def uppCons(frase):
    '''Dado uma frase, retorna todas as suas consoantes maiúsculas.
str --> str'''
    a = len(frase)
    b = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    proximo = 0
    while proximo < a:
        if frase[proximo] in b:
            str.upper(frase[proximo])
        proximo = proximo + 1
    return frase