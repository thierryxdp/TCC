def qtd_divisores(num):
    qtd_d=[]
    for divisor in range(1,num+1): #lista de valores de 1 até num, desses quais d sera os divisores 
        if num%divisor==0:
            list.append(qtd_d,divisor)
    return len(qtd_d)