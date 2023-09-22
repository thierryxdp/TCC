def soma_h(n):
    """ calcula a H baseado na entrada N"""
    h=0
    for i in range(1,n+1):
        h=h+1/i
    return round(h,2)