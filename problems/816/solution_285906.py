def maiores(lista,n):
    ''' Função que retorna uma lista de números de uma lista original 
    maiores que o numeral 'n'.    list=>list'''
    lista.insert(0,n)
    list.sort(lista)
    filtrado = filter(lambda num: num > n, lista)
    return (list(filtrado))