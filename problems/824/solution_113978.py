def uppCons(frase):
    '''Função que altera para maiúscula todas as consoantes 
    da frase dada e o restante da frase permanece da mesma
    forma.
    str -> str'''
    nova_frase=''
    vogal='AEIOUaeiou'
    i=0
    while i<=len(frase):
        if frase[i] in 'AEIOUaeiou':
            return frase
        if frase in not 'AEIOUaeiou':
            return str.upper[frase]
        i=i+1
    return nova_frase''