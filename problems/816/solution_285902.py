def maiores(lista,n):
    ''' Função que retorna uma lista de números de uma lista original 
    maiores que o numeral 'n'.    list=>list'''
    lista.insert(0,n)
    list.sort(lista)
    [n for n in lista if int < n]