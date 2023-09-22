def carros(n,c):
    "Retorna o número de carros necessário para n pessoas, e cada carro com capacidade c"
    if len(n,c)==1:
        if (n//5)==0:
            return 1
        if (n%5)!=0:
            return (n//5)+1 
        if (n%c)==0:
            return n//c
    if len(n,c)==2:
        if (n//c)==0:
            return 1
        if (n%c)!=0:
            return (n//c)+1
        if (n%c)==0:
            return n//c