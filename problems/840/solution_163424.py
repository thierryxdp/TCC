def bolos(a,b,c):
    "calcula a quantidade de bolos que podem ser feitos com o numero de materias ensirods"
    if a == 0 or b == 0 or c == 0:
        return 0
    else:
        return (a+b+c)//10