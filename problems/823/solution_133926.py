def faltante(lista):
    """Determina qual o número da peça do quebra-cabeça
    que está faltando;
    list -> int"""
    i=1
    list.sort(lista)
    
    if lista[0] != 1:
      	return 1
    
    while i < len(lista):
        if lista[i] - lista[i-1] == 2:
            return lista[i-1]
        i +=1
        
    if lista[0] == 1:
        return lista[-1]+1