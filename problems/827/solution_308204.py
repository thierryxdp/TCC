#Essa função conta a quantidade de divisores que um número tem.
#int->int
def qtd_divisores(num):
    divisor=1
    contador=0
    while num>divisor:
        if num%divisor==0:
            contador+=1
        divisor+=1
    return contador