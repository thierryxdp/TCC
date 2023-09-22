def uppCons(frase):
    '''Função que, dada uma string de entrada, retorna a mesma string
    apenas com as consoantes em maiúsculo. str -> str'''
   
    x=list(frase)
    proximo=0

    while proximo<len(x):
        if x[proximo] in 'bcdfghjklmnpqrstvwxyzç':
            x[proximo]=str.upper(x[proximo])
           
        proximo=proximo+1

    return ''.join(x)