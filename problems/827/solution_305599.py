def qtd_divisores(num):
    " " "Conta a quantidades de divisores um número tem; int, -> int" " "
    resultado=0
    for i in list(range(1, num+1)):
        if num % i == 0: 
             resultado = resultado + 1
    return resultado