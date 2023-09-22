def uppCons(x):
    '''
    '''
    listaCons=[]
    proximo=0
    while proximo<len(x):
        if x[proximo] not in 'aeiouAEIOUãóúí':
            listaCons= listaCons+ [str.upper(x[proximo])]
        else:
            listaCons= listaCons+ [x[proximo]]
        proximo=proximo+1
    return str.join('',listaCons)