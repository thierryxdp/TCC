def decres(listad, num):
   
    listad.append(num)
    listad.sort(reverse=True)
    
    
def maiores(lista, n):
     """Função que dada uma lista de inteiros e um número inteiro n, retorna outra lista que tenha todos os itens da lista original maior que n 
  	   list, int -> list
    """
    lista_toda = decres(lista,n)
    nova_lista = [ elem for elem in lista_toda if elem > n ]
    
    return nova_lista