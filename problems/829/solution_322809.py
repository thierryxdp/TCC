def soma_h(n):
    '''Função que retorna a soma de frações até 1/n 
    com até duas casas decimais
    entrada=int
    saida= float'''
    h=[]
    for x in list(range(1,n+1)):
        list.append(h, 1/x)
    return round(sum(h),2)