def maiores (lista_de_numeros,numero):
    '''Dado uma lista de números inteiros e um número inteiro,
    retorna outra lista, que contenha todos os números da lista original
    maiores que o número dado, ordenados em ordem crescente;
    list, int -> list'''
    if numero in lista_de_numeros: 
        list.sort(lista_de_numeros)
        lista_de_numeros1=list.index(lista_de_numeros,numero)
        return lista_de_numeros[lista_de_numeros1+1:]
    else: 
        list.append(lista_de_numeros,numero)
        list.sort(lista_de_numeros)
        lista_de_numeros1=list.index(lista_de_numeros,numero)
        return lista_de_numeros[lista_de_numeros1+1:]

def acima_da_media(lista_de_notas):
    '''Dado uma lista com as notas dos alunos de uma turma,
    a função irá retornar uma lista ordenada com as notas 
    que ficaram acimada média;
    list -> list'''
    
    media_de_notas=(sum(lista_de_notas))/(len(lista_de_notas))
    
    return maiores(lista_de_notas,media_de_notas)