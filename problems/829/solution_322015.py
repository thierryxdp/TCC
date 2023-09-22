def func(x):
    return int(1/x)

def soma_h(n):
    " " "Calcula e retorna o valor H com 'n' termos;H=1+(1/2)+(1/3)+...+(1/n);int, -> float " " "
	lista = []
    for i in list(range(1,n+1)):
        lista.append(1/i)
    resultado = sum(map(func,lista)) 
    return round(resultado,2)