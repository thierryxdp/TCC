def soma_h(n):
    """calcula o valor de H baseado na entrada N"""
    h=0
    for i in range(i,n+1):
        h=h+1/i
    return round(h,2)