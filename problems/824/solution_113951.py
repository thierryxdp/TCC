def uppCons(frase):
    '''Função que altera todas as consoantes da frase dada
para maiúscula e o restante da frase permanece da mesma forma.
str -> str'''
    nova_frase=''
    vogal='AEIOUaeiou'
    i=0
    while i<=len(frase):
        if frase[i] in 'AEIOUaeiou':
            return frase[i]
        if frase in not 'AEIOUaeiou':
            return str.upper[i]
        i=i+1
    return nova_frase''