#
#
#
#
def qtd_divisores(n):
    tot_div=0
    i=1
    while i<=n:
        if n%i==0:
            tot_div=tot_div+1
        i=i+1
    return tot_div