def lingua_p(palavra):
    '''Dada uma palavra da lingua portuguesa, a função adiciona, a
    cada vogal, a letra p mais a vogal em questão. str --> str'''
   
    L = list(palavra)
    P=[]
   
    for letra in L:
        if letra in 'AEIOUaeiouáéíóúãâô':
            P=P+[letra+'p'+letra]
        else:
            P=P+[letra]
   
    return ''.join(P)