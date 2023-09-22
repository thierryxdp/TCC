def maiores(lista_numero, n):
    """ define uma lista que retorna outra lista que contenha todos os numeros da lista original maiores que n em ordem crescente"""
    if n not in lista_numero:
        lista_numero = lista_numero + [n]
        lista_numero = sorted(lista_numero)
        x= list.index(lista_numero, n)
        return lista_numero[(x+1):len(lista_numero)]
    else:
        lista_numero = sorted(lista_numero)
        x= list.index(lista_numero,n)
        return lista_numero[(x+1):len(lista_numero)]
    
    
    def acima_da_media(notas):
        """ Retorna uma função que dada uma lista com nota dos alunos retorna uma lista ordenada com as notas que ficaram acima da média"""
        media = sum(notas)/len(notas)
        return maiores(notas, media)