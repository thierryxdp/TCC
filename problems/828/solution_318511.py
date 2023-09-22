def primo(n):
    '''Recebe um número e quantifica seus divisores;
    int -> int'''
    d = 1 
    a = 0
    while d <= n:
        if n%d == 0:
            if d > 2 and d < n:
            	a = a
            elif d == 1 or d == n:
                a = a + 1
        d = d + 1
            
    return bool(a)