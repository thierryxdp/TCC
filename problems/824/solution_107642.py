def uppCons(frase):
    '''Dado uma frase, retorna todas as suas consoantes maiúsculas.
str --> str'''
    a = frase[:]
    b = len(a)
    c = ['b','c','ç','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    proximo = 0
    while proximo < b:
        if a[proximo] in c:
            a = str.replace(a,a[proximo],str.upper(a[proximo]))
        proximo = proximo + 1
    return a