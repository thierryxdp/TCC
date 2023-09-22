def colchao(medidas: list[int], h : int, l : int) -> bool:
    """funcao que ,para resolver o problema de passar o colchao pela porta de casa,recebe medidas  com os tamanhos inteiros da altura e largura da porta e valida se o item passa ounao;int,int->bool"""
    
    if (medidas[1] <= h and medidas[2] >= l)or(medidas[1]>=h and medidas[2]<=l)or(medidas[1]<=h and medidas[2]<=l):
        
        
        return True
    else:
        return False