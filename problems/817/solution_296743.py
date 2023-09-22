def maiores(lista,n):
    """funcao que dada uma lista de numeros inteiros e um 
    numero inteiro n de entrada, retorna outra lista, que
    contenha todos os numeros da lista original maiores que 
    n ordenados em ordem crescente;
    list, int -> list"""
    
    lista2 = []
    for i in lista:
        if i>n:
            list.append (lista2,i)
    list.sort(lista2)
    return lista2
         
def acima_da_media(lista_nota):
    """funcao que dada uma lista com as notas dos alunos de entrada
    retorna uma lista ordenada com as notas que ficaram acima da
    media;
    list -> list"""
    
    media = sum(lista_nota)/(len(lista_nota))
    return maiores(lista_nota,media)