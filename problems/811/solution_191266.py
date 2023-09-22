def passa_da_porta(colchao,H,L):
    'dadas as dimensoes do colchao e da porta, retorna se o colchao passa por ela ou nao list,int->bool'
    if colchao[0]<L and colchao[1]<H:
        return 'True'
    else:
        return 'False'