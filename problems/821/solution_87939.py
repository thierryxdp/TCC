def fatorial(n):
    " " "Calcula a fatorial de um número n;int, -> int " " "
    resultado=1
    count=1
    while count <= n:
        resultado *= count
        count += 1
    return resultado