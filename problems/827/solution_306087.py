def qtd_divisores(n):
    """Função que calcula quantos divisores tem um número
    int -> int"""
    x = [1] * (n +1);
    y = 2;
    if n > 0:
        while((y * y) < n):
            if (x[y] == 1):
                for i in range((y * 2), n, y):
                    x[i] = 0;
            y += 1;
        dvsrs = 1;
        for y in range(2, n+1):
            if (x[y] == 1):
                
            z = 0
            if (n%y ==0):
                while (n%y == 0):
                    n = int(n/y);
                    z += 1;
                dvsrs *= (z+1);
        return dvsrs
    else:
        return 0