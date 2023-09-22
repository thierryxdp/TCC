def filtra_pares(tupla):
    ''' Função que recebe uma tupla com quatro números inteiros e só retorna
    dentre eles os que são pares. tuple(int,int,int,int) -> tuple(int,int,int,int)'''
    tupla_par = ()
    x0,x1,x2,x3 = tupla[0],tupla[1],tupla[2],tupla[3]
    if x0%2==0 and x1%2==0 and x2%2==0 and x3%2==0:
        tupla_par = (x0,x1,x2,x3)
        return tupla_par
    elif x0%2!=0 and x1%2!=0 and x2%2!=0 and x3%2!=0:
        return tupla_par
    elif x0%2!=0 and x1%2==0 and x2%2==0 and x3%2==0:
        tupla_par=(x1,x2,x3)
        return tupla_par
    elif  x0%2!=0 and x1%2!=0 and x2%2==0 and x3%2==0:
        tupla_par = ( x2,x3)
        return tupla_par
    elif  x0%2!=0 and x1%2!=0 and x2%2!=0 and x3%2==0:
        tupla_par = (x3)
        return tupla_par
    elif  x0%2==0 and x1%2==0 and x2%2==0 and x3%2!=0:
        tupla_par = (x0,x1,x2)
        return tupla_par
    elif  x0%2==0 and x1%2==0 and x2%2!=0 and x3%2!=0:
        tupla_par = (x0,x1)
        return tupla_par
    elif  x0%2==0 and x1%2!=0 and x2%2!=0 and x3%2!=0:
        tupla_par = (x0)
        return tupla_par
    elif  x0%2==0 and x1%2!=0 and x2%2==0 and x3%2==0:
        tupla_par=(x0,x2,x3)
        return tupla_par
    elif  x0%2==0 and x1%2!=0 and x2%2!=0 and x3%2==0:
        tupla_par = (x0,x3)
        return tupla_par
    elif  x0%2!=0 and x1%2==0 and x2%2!=0 and x3%2!=0:
        tupla_par = (x1)
        return tupla_par
    elif  x0%2!=0 and x1%2!=0 and x2%2==0 and x3%2!=0:
        tupla_par(x2)
        return tupla_par
    elif  x0%2==0 and x1%2!=0 and x2%2==0 and x3%2!=0:
        tupla_par=(x0,x2)
        return tupla_par
    elif  x0%2!=0 and x1%2==0 and x2%2!=0 and x3%2!=0:
        tupla_par=(x1,x3)
        return tupla_par