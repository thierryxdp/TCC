def maiores(lista_inteiros,n):
# Ao fornecer uma lista de números inteiros e um outro inteiro n, retorna uma nova
#lista com os numeros da lista original maiores que n.

#list, int -> list

    lista_nova = list.copy(lista_inteiros)

    list.sort(lista_nova)
    
    indice = list.index((lista_nova,n)+1)

    return lista_nova[indice:]

	#encontra qual é a posição de n na lista e soma-se 1 para ler valores acima de n
    #até o final da lista