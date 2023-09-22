def uppCons(fra):
    i = 0
    lis = list(fra)
    '''vogais = "AÁÀÃÂEÉÈÊIÍÎÌÓÒÔÕOUÚÙÛaáàâãeéèêiíìîóòõôuúùû"'''
    
    while i < len(fra):
        if lis[i] not in "aeiouáéíóúÁÉÍÓÚAEIOU":
            lis[i] = str.upper(lis[i])
            i += 1
        else:
            i += 1
    return str.join('', lis)