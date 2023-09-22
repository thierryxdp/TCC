def uppCons(frase):
    '''Função que recebe a frase e altera para maiúscula 
    todas as consoantes da frase dada e o restante da frase 
    permanece da mesma forma.
    str -> str'''
    nova_frase=''
    vogal='AEIOUaeiou'
    i=0
    while i<=len(frase):
        if frase[i] in 'AEIOUaeiou':
            return frase
        else:
            return str.upper[i]
        i=i+1
    return nova_frase''