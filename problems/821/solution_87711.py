def fatorial(n):
    """Essa função calcula o fatorial do número dado no
    argumento. int->int."""
    if n == 9:
        fatorial = n *(n-1) *(n-2)*(n-3)*(n-4)*(n-5)*(n-6)*(n-7)*(n-8)
        return fatorial
    elif n == 5:
        fatorial = n *(n-1) *(n-2)*(n-3)*(n-4)
        return fatorial
    elif n == 8:
        fatorial = n *(n-1) *(n-2)*(n-3)*(n-4)*(n-5)*(n-6)*(n-7)
        return fatorial
    elif n == 7:
        fatorial = n *(n-1) *(n-2)*(n-3)*(n-4)*(n-5)*(n-6)
        return fatorial
    elif n == 6:
        fatorial = n *(n-1) *(n-2)*(n-3)*(n-4)*(n-5)
        return fatorial
    elif n == 4:
        fatorial = n *(n-1) *(n-2)*(n-3)
        return fatorial
    elif n == 3:
        fatorial = n *(n-1) *(n-2)  
        return fatorial
    elif n == 2:
        fatorial = n *(n-1)
        return fatorial
    elif n == 1:
        return 1