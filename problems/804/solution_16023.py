def filtra_pares(t):
    '''funçao que recebe 4 elementos e retorna somente os pares;
    string-> string''' 
    if t[0] % 2 == 0:
        a = t[0]
    if t[1] % 2 == 0:
        b = t[1]
    if t[2] % 2 == 0:
        c = t[2]
    if t[3] % 2 == 0:
        d = t[3]
    y = int(a) + int(b) + int(c) + int(d)    
    
    
    return y #Start your python function here