def carros(n):
    "Retorna o número de carros necessário para n pessoas, e cada carro com capacidade c"
    if (n//5)==0:
        return 1
    if (n%5)!=0:
        return (n//5)+1