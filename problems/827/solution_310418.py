def qtd_divisores(x):
    '''retorna quantos divisores um numero inteiro de
    entrada x tem
    int -> int'''
    divi = 0
    for i in range (1,x):
        if(x%i==0):
            divi +=1
            return divi
        if divi <= 0:
            return 0