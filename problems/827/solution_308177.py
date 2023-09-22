def qtd_divisores(numero):
    resultado=[]
    if numero>0:
        for i in range(1,100000):
            if numero%i==0:
                list.append(resultado,i)
        return len(resultado)
    else:
        return 0