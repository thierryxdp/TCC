def qtd_divisores(n):
    
    if n == 0:
        print('Erro 404')
    else:
        contadorDivisores = 1
        for i in range(1, n):
            
            #Pegando o resto da divisão
            # Se for 0 significa que o numero "n" tem um divisor
            if n%i==0:
                contadorDivisores += 1
        print("Total de divisores: ", contadorDivisores)        

qtd_divisores(0)
qtd_divisores(4)
qtd_divisores(5)
qtd_divisores(7)
qtd_divisores(10)
qtd_divisores(20)