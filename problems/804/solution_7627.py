def filtra_pares(a):
    '''funcao que recebe uma tupla com 4 numeros inteiros e retorna uma nova tupla contendo apenas os elementor pares;tuple-->tuple'''
    if int(a[0])%2==0:
        z=int(a[0])
        if int(a[1])%2==0:
            x=a[1]
            if int(a[2])%2==0:
                c=a[2]
                if int(a[3])%2==0:
                    v=a[3]
                    return z,x,c,v