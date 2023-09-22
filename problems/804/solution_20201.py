#Start your python function here
def filtra_pares(a):
    if a[0]%2==0:
        primeiro=a[0]
    if a[1]%2==0:
        segundo=a[1]
    if a[2]%2==0:
        terceiro=a[2]
    if a[3]%2==0:
        quarto=a[3]
    pares_novo=(primeiro,segundo,terceiro,quarto)
    return pares_novo