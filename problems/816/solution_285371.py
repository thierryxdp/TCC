def maiores(l, n):
    'Recebe uma lista e um numero, ordena a lista em ordem alfabetica,' 
    'adiciona o numero a ela,'
    'e retorna somente os numeros maiores que n list->list'
    l= l + [n]
    list.sort(l)
    p=l.index(n)
    l=l[p:] 
    l.pop(0)
    return l