def carros(*arg):
    "Retorna o número de carros necessário para n pessoas, e cada carro com capacidade c"
    n=arg[0]
    if len(arg)==1:
        c=5
    else:
        c=arg[1]
    if n%c==0:
        return n//c
    if n%c!=0 or n//c==0:
        return (n//c)+1