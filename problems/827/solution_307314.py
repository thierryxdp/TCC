def qtd_divisores(i):
    l = []
    for n in range(1, i+1):
        if i % n == 0:
            list.append(l, n)
    return len(l)
#Testes:
#qtd_divisores(200)--> 12
#qtd_divisores(2)--> 2
#qtd_divisores(17)--> 2
#qtd_divisores(2800)--> 30
#qtd_divisores(15)--> 4
#qtd_divisores(10)--> 4