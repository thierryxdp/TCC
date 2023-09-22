# A função recebe um número inteiro N e retorna quantos divisores esse número tem
# int-->int
#
#
def qtd_divisores(N):
    tot_div=0
    i=1
    while i<=N:
        if n%i==0:
            tot_div=tot_div+1
        i=i+1
    return tot_div