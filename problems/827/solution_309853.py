# função recebe um número e retorna a quantidade de divisores que possui.
# int --> int
def qtd_divisores(num):
    contador=0
    for i in range(1,num+1):
        if i%num==0:
            print(i)