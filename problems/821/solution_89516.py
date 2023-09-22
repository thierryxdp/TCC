def fatorial(num):
    '''calcula o fatoria de num
    int->int'''
    cont=num
    while cont>=1:
        num=num*(num-1)
        cont=cont-1
    return num