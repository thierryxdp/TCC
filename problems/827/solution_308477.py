def qtd_divisores(n):
    '''função que conta quantos divisores um número tem,sendo esse número passado como entrada; int -> int'''
    y=range(1,n+1)
    div=0
    for d in y:
        if n%d==0:
            div+=+1
    return div