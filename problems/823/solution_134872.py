def faltante(lista):
    """
    Função que recebe uma lista e retornaremos o valor faltante no seu intervalo.
    Para isso, utilizaremos as fórmulas da PA para encontrar valores faltantes em intervalos
    definidos e finitos.
    list -> int
    """
    
    i = 0 
    tamanho_lista = len(lista)
    pa = tamanho_lista + 1
    soma_pa = pa * (pa+1)//2
    total_pecas = sum(lista)
    
    return soma_pa - total_pecas