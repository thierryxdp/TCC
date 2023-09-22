def qtd_divisores(n):
    '''funç˜ao que conta quantos divisores um dado número inteiro 'n' tem.
       int->int '''
    lista=[]
    for numero in range(1,n+1):
        if n%numero==0:
            list.append(lista,numero)
    return len(lista)