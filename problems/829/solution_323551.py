def soma_h(n):
    '''Esta função calcula o valor de h, sendo h o somatório das divisões de 1/x, começando por x=1 até n.
int->int'''
    h=0
    for x in range(1,n+1):
        h+=1/x
    return round(h,2)