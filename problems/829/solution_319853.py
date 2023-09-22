def soma_h(t):
    '''calcula o somatorio de n termos 
    int -> float'''
    a=0
    b=1
    for b in range(1,t+1):
        a=a+1/b
    return round(a,2)