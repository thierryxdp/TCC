def filtra_pares(x):
    '''calcula e filtra os pares de uma função'''
    if x[1]/2==0:
        return x
    else:
        return x-x[0]
    if x[2]/2==0:
        return x
    else:
        return x-x[1]
    if x[3]/2==0:
        return x
    else:
        return x-x[2]
    if x[4]/2==0:
        return x
    else:
        return x-x[3]