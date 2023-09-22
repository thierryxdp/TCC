def filtra(x):
    return x % i == 0

def qtd_divisores(num):
    " " "Conta a quantidades de divisores um número tem; int, -> int" " "
	valores = []
    for i in list(range(1, num+1)):
        valores.append(i)
    resultado = len(filter(filtra,valores))               
    return resultado