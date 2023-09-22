def colchao(medidas,H,L):
    '''dadas as medidas dos colchoes(crescentes e em ordem) e retorna se o colchao passa ou nao pela porta; lis, int, int -> bool'''
    if medidas[0]<-L and (medidas[1]<-H or medidas[1]<-L):
        return True
    else:
        return False