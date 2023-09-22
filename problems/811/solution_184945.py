def colchao(medidas,H,L):
    '''função que dada as dimensões de um colchão em valores inteiros
    e em ordem crescente e a altura H da porta e largura L da porta
    retorna true se é possivel passar o colchão pela porta e false 
    caso contrário;
    list,int,int-->bool'''
    s=medidas
    if s[1]<H and s[0]<L:
        return True
    else:
        return False