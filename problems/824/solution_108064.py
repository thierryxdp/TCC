def uppCons(frase):
    '''recebe uma frase retorna a mesma frase com as consoante em caixa alta'''
    frasef=''
    i=0
    while i<len(frase):
        if frase[i] in 'bcçdfghjklmnpqrstvwxyz':
            frasef+=frase[i].upper()
        else:
            frasef+=frase[i]
        i+=1
    return frasef