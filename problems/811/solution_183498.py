def colchao(lista,H,L):
    """Faça uma função para resolver o problema, onde medidas é uma lista com 
    tamanhos inteiros A, B e C, e H e L são os tamanhos inteiros da altura e largura da porta."""
    
    maior = max(H,L)
    menor = min(H,L)
    
    if (lista[1]) > maior):
        return False
    else:
        return True