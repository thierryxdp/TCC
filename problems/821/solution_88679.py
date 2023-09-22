def fatorial(n):
    '''calcula o fatorial de um num
    int -> int'''
    
    f=1
    i=1
    
    while i <= n:
        f=f*i
        i=i+1
        
    return f