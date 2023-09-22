#Start your python function here
def filtra_pares(a):
    even_numbers=()#cria uma nova tupla com os numeros pares
    if a[0]%2==0:#faz o modulo de cada caractere da tupla
        even_numbers+=(a[0],)#se o caractere for par, adciona ele na tupla
    if a[1]%2==0:
        even_numbers+=(a[1],)
    if a[2]%2==0:
        even_numbers+=(a[2],)
    if a[3]%2==0:
        even_numbers+=(a[3],)
    return even_numbers ##retorna todos os numeros pares