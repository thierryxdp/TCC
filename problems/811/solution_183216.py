def colchao(medidas,H,L):
    '''
        Função que, com as medidas enviadas de um colchão, retorna se ele passa ou não pela porta da casa.
        Int,Int,Int,Int,Int => Bolean
    '''
    medidas.sort()
    porta = [H, L]
    porta.sort()

    if(medidas[0] <= porta[0] and medidas[1] <= porta[1]):
        return 'True'
    else:
        return 'False'