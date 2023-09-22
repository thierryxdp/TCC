def filtraMultiplos(lista_entrada,num):
    """Dada uma lista de números inteiros e um número inteiro qualquer x, respectivamente, essa função retorna uma outra lista contendo os múltiplos de x presentes na lista original; list, int -> list"""
    contador = 0
    lista_multiplos = []
    
    while contador<len(lista_entrada):
        if lista_entrada[contador]%num==0:
            list.append(lista_multiplos,lista_entrada[contador])
        contador = contador+1
    return lista_multiplos