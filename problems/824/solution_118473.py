def uppCons(x):
    '''
    função que recebe como entrada uma frase (x) e retorna a frase com todas as suas 
    consoantes em maiusculo.
    str->str
    '''
    listaCons=[]
    proximo=0
    while proximo<len(x):
        if x[proximo] not in 'aeiouãóúíé':
            listaCons= listaCons+ [str.upper(x[proximo])]
        else:
            listaCons= listaCons+ [x[proximo]]
        proximo=proximo+1
    return str.join('',listaCons)