def colchao(medidas,H,L):
    '''Funcao que delimita se um colchao poderá ou não passar
pela porta de acordo com as medidas, de forma crescente, do 
colchão em [A,B,C] e da porta como H altura e L largura;
	list,int,int -> booleano.'''
    A=medidas[0]
    B=medidas[1]
    if A<=L and B<=H:
        return 'True'
    else:
        return 'False'