def soma_h (n):
    '''retorna o valor de H baseado na formula utilizando o termo n
    int->flaot'''
    j=0
    i=1
    while i <= n:
        j=j+(1/i)
        i=i+1
    return round(j,2)