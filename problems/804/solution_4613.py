def filtra_pares(tupla):
    """Essa função irá receber uma tupla com quatro elementos inteiros e irá retornar uma nova tupla contendo apenas os elementos pares da tupla original"""
    elemento1 = tupla[0]
    elemento2 = tupla[1]
    elemento3 = tupla[2]
    elemento4 = tupla[3]
    
    nova_tupla = []
    
    if elemento1 % 2 == 0:
        nova_tupla.append(elemento1)
    
    if elemento2 % 2 == 0:
        nova_tupla.append(elemento2)
        
    if elemento3 % 2 == 0:
        nova_tupla.append(elemento3)
        
    if elemento4 % 2 == 0:
        nova_tupla.append(elemento4)
        
    return tuple(nova_tupla)