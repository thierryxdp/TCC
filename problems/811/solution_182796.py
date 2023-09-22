def colchao (medidas,H,L):
    '''funcao que dado as dimecoes do colchao verifica se ele
    passa pela porta dada as medidas da mesma; 
    int,int,int -> bool'''
    (a,b,c) = medidas
    if b<=H:
        return True
    else:
        return False