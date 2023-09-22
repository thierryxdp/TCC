def soma_h(N):
    '''A função retorna a soma de frações, tendo 1 como dividendo e 0 até N como divisor
    int -> float'''
    h = 0
    i = 1
    while i<=N:
        h = h + 1/i
        i = i+1
    return round(h,2)