def uppCons(frase):
    '''Função que retorna todas consoantes da frase fornecida em maiúsculas
    e os demais caracteres permanecem no mesmo formato
    str=> str'''
    i=0
    frase_ajuste=''
    while i<len(frase):
        if frase[i} in 'bcdfghjklmnpqrstvwxyzç':
                 frase_ajuste+=frase[i].upper()
        else:
            frase_ajuste+=frase[i]
        i+=1
    return frase_ajuste