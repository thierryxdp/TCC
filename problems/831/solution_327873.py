def lingua_p(palavra):
    '''função que dada uma palavra em português retorna a mesma palavra 
    na língua do P;
    str-->str'''
    vogais='AEIOUaeiou'
    for letra in 'palavra':
        if letra in vogais:
            str.replace(palavra,'letra','letra'+'p'+'letra')
            str.replace(vogais,'letra','')
    return palavra