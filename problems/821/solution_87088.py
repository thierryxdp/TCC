def fatorial(n):
    "Calcula o fatorial de n. list->int"
    fat = 1
    i = 2
    while i<=n:
        fat = fat*i
        i+=1
    return fat