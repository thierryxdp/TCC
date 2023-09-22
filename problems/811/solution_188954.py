def colchao(medidas,H,L):
    '''Calcula e retorna se o colchão de dimensões da lista
       de entrada 'medidas' passa pela porta de altura 'H' e
       e de largura 'L';
       list, float, float -> bool'''
    if medidas[0] <= L and medidas[1] <= H:
        return True
    False