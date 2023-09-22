def fatorial(n):
    '''calcula a fatorial do numero desejado;
    int->int'''
    fat=1
    while 0<n:
        fat=n*fat
        n=n-1
    return fat