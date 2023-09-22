def fatorial(num):
    '''calcula o fatoria de num
    int->int'''
    cont=0
    num=num+1
    multiplicacao=1
    while cont!=num:
        multiplicacao=multiplicacao*(num-1)
        cont=cont+1
    return multiplicacao