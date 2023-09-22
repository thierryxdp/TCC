def soma_h(n):
    " " "Calcula e retorna o valor H com 'n' termos;H=1+(1/2)+(1/3)+...+(1/n);int, -> float " " "
    resultado = 0
    for i in list(range(1,n+1)):
        resultado = resultado + (1/i)
    return round(resultado,2)