def conta_numero(numero,matriz):
   '''função que dado um número inteiro e uma matriz, conta a quantidade de vezes que aquele aparece na matriz'''
c= 0
for l in matriz:
    for co in l:
        if numero== co:
            c= c+ 1
return c