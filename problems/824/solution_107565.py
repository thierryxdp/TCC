def uppCons(frase):
    '''Dado uma frase, retorna todas as suas consoantes maiúsculas.
str --> str'''
    a = list(frase)
    b = len(a)
    c = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    d = ''
    proximo = 0
    while proximo < b:
        if a[proximo] in c:
            d = d + str.upper(a[proximo])
        proximo = proximo + 1
    return d