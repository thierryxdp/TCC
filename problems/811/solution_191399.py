def colchao(Col,H,L):
    'Recebe as medidas de um colchão retorna se ele passaria ou não por uma porta.'
    'lista->booleano'
    A=Col[0]
    B=Col[1]
    
    if (H>=A and L>=B) or (H>=B and L>=A):
        return True
    else:
        return False