#Essa função avalia se um número é primo ou não.
#int->booleano
def primo(num):
    divisor=1
    contador=0
    while num>=divisor:
        if num%divisor==0:
            contador+=1
        divisor+=1
        
    return contador == 2