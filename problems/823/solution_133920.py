def faltante(lista):
    """Determina qual o número da peça do quebra-cabeça
    que está faltando;
    list -> int"""
    i=1
    list.sort(lista)
    
    while i < len(lista):
        if lista[i] - lista[i-1] == 2:
            return lista[i]
        i +=1