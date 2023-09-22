def colchao(medidas,H,L):
     '''Função que verifica se é possível ou não de passar o
    colchão pela porta da casa.
    A=espessura do colchao
    B=largura do colchao
    C=comprimento do colchao
    H=altura da porta
    L=largura da porta
    float,float,float ->str'''
        if medidas[2] <H:
            return True
        if medidas[2]<L:
            return True
        if medidas[3]<H:
            return True
        if medidas[3]<L:
            return True