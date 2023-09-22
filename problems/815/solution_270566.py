def insere(lista_numero,n):
    """Retorna uma lista sendo igual à lista que é o primeiro parâmetro acrescida do elemento n, que é o segundo parâmetro, mas em ordem crescente;
    list,int->list"""
    a=list(str(n))
    a[0]=int(a[0])
    return list.sort(lista_numero+a)