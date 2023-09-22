def passa_da_porta(dimcolchao,H,L):
    'dadas as dimensoes do colchao e da porta, retorna se o colchao passa por ela ou nao list,int->bool'
    if dimcolchao[0]<L and dimcolchao[1]<H:
        return 'True'
    else:
        return 'False'