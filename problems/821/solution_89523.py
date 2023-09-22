def fatorial(num):
    '''calcula o fatoria de num
    int->int'''
    cont=0
    limite=num
    multiplicacao=1
    while cont!=limite:
        multiplicacao=multiplicacao*(num)
        cont=cont+1
        num=num-1
    return multiplicacao