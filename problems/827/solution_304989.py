def qtd_divisores(n):
    
    if n == 0:
        print('Erro 404')
    else:
        cont = 1
        for i in range(1, n):
            if n%i==0:
                cont += 1
        print("Total de divisores: ", cont)        

qtd_divisores(0)
qtd_divisores(4)
qtd_divisores(5)
qtd_divisores(7)
qtd_divisores(10)
qtd_divisores(20)