def primo(n):
    contador = 0
    for i in range(1, n):
        conta = n%i
        situacao = bool(conta==0)
            if situacao == True:
                contador = contador + 1
        resultado = bool(contador==1)
                
    return Resultado