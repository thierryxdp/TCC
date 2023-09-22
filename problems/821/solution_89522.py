def fatorial(num):
    '''calcula o fatoria de num
    int->int'''
    cont=0
    limite=num
    num=num+1
    multiplicacao=1
    while cont!=limite:
        multiplicacao=multiplicacao*(num-1)
        cont=cont+1
    return multiplicacao