def maiores(lista, n):
    """Função que dada uma lista de inteiros e um número inteiro n, retorna outra lista que tenha todos os itens da lista original maior que n 
  	   list, int -> list
    """
    
    lista.append(n)
    lista.sort(reverse=True)
    
    return lista