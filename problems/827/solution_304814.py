def qtd_divisores(n):
    """Recebe um número e retorna quantos divisores esse número possui
       parâmetro de entrada:int
       parâmetro de saída:int"""
    i=1
    lista=[]
    for i in range(1,n//2+1):
        if (n%i==0):
            list.append(lista,i)
    return len(lista)