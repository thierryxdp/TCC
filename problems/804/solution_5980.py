def filtra_pares(tupla):
    """Função que recebe uma tupla, com quatro números como parâmetro, e retorna
    uma nova tupla com apenas números pares da tupla original, na mesma ordem;
    tuple[int,int, int, int] -> tuple"""
    valor1 = tupla[0]
    valor2 = tupla[1]
    valor3 = tupla[2]
    valor4 = tupla[3]
    if valor1%2==0 and valor2%2==0 and valor3%2==0 and valor4%2==0:
        return valor1,valor2,valor3,valor4
    elif valor1%2==0 and valor2%2 ==0 and valor3%2 == 0:
        return valor1,valor2,valor3
    elif valor1%2==0 and valor2%2==0 and valor4%2 == 0: 
        return valor1, valor2, valor4
    elif valor1%2==0 and valor3%2==0 and valor4%2 == 0 :
        return valor1, valor3, valor4
    elif valor2%2==0 and valor3%2==0 and valor4%2 == 0:
        return valor2,valor3,valor4
    elif valor1%2 == 0 and valor2%2 == 0: 
        return valor1,valor2
    elif valor1%2 == 0 and valor3%2 == 0: 
        return valor1,valor3
    elif valor1%2 == 0 and valor4%2 == 0:
        return valor1,valor4
    elif valor2%2 == 0 and valor3%2 == 0 :
        return valor2,valor3
    elif valor2%2 == 0 and valor4%2 == 0 :
        return valor2,valor4
    elif valor3%2 == 0 and valor4%2 == 0 :
        return valor3,valor4
    elif valor1%2 == 0 and not (valor2%2==0 and valor3%2==0 and valor4%2 == 0):
        return valor1,
    elif valor2%2 == 0 and not (valor1%2==0 and valor3%2==0 and valor4%2 == 0):
        return valor2,
    elif valor3%2 == 0 and not (valor1%2==0 and valor2%2==0 and valor4%2 == 0):
        return valor3,
    elif valor4%2 == 0 and not (valor1%2==0 and valor2%2==0 and valor3%2 == 0):
        return valor4,
    else:
        return ()