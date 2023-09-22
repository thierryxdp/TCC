def lingua_p(P):
    '''Calcula e retorna a palavra(P) para a língua do p,adicionando um p após uma vogal e adicinando também essa mesma vogal após o p.
    str-->str'''
    r=''
    for i in range(len(P)):
        if P[i] not in 'bcdfghjklmnpqrstvxwyz':
            n=P[i]+'p'+P[i]
            r=r+n
        if P[i] in 'bcdfghjklmnpqrstvxwyz':
            r=r+P[i]
    return r