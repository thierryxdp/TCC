def Edivisivel(n):
    	return True if num % n == 0 else False    

def qtd_divisores(num):
    global num
    lista = list(range(1, num + 1))
    filtrado = list(filter(Edivisivel, lista))
    return len(filtrado)