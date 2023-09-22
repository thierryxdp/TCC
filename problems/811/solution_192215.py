def colchao(medidas,H,L):
    '''Dadas a altura e largura de uma porta e as medidas de um
    colchão na forma de um paralelepípedo reto retângulo (em centímetros),
    a função retorna se será possível passar o colchão pela porta
    com uma de suas faces paralela ao chão.
    list,int,int -> bool'''
    #[A,B,C],H,L
    if (medidas[0]<H or medidas[1]<L) or (medidas[0]<L or medidas[1]<H):
        return True
    else:
        return False