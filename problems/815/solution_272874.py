def insere(a,b):
    ' adiciona um número inteiro na lista e ordena ela de forma crescente'
    'entrada: list,int'
    'saida: list'
    x=a
    x.append(b)
    list.sort(x)
    return x
insere([45,63,89],53)