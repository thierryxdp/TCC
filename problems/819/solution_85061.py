def filtramultiplos(numero,n):
    cont=0
    num=[]
    while cont<len(numero):
        if numero[cont]%n==0:
            num=num+[numero[cont]]
        cont=cont+1   
    return num