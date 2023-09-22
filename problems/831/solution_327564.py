def lingua_p(palavra):
    i=0
    k=''
        for palavra[i] in 'bcdfghjklmnpqrstvwxyz':
            k=''.join(palavra[i])
        i=i+1
    return k