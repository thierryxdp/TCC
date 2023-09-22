def filtra_pares(x):
    '''calcula e filtra os pares de uma função'''
    def par1(x):
        if x[1]/2==0:
            return x[1]
        else:
            return ()
    if x[0]/2==0:
        return x[0]+par1(x)
    else:
        return par1