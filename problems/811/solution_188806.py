def colchao(medidas, H, L):
    '''Retorna se é possível um determinado colchão (com 
    suas medidas especificadas em ordem crescente na lista 
    'medidas') passar pela porta de altura H e largura L
    list, float, float -> bool'''
    if H<L:
       if (medidas[1] > L):
           return False
       else:
           return True
    if L<H:
       if (medidas[1] > H):
           return False
       else:
           return True