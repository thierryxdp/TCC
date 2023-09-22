#int -> booleano
def primo(num):
    #criar contador de divisores
    contador=2
    #definir se num tem divisores ou não
    for d in range(2,(round(num**(1/2)))):
        if num%d==0:
            contador+=1
    if contador!=0:
        return False
    return True