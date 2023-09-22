def qtd_divisores(n):
    """
    Ao inserir um número, o código retornará a
    quantidade de divisores esse número tem. 
    Caso o número seja negativo,o resultado será 0
    int->int
    """
    resultado=[]
    if n>0:
        for i in range(1,1000):
            if n%i==0:
                list.append(resultado,i)
        return len(resultado)
    else:
        return 0