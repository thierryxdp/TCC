def fatorial(numero:int)->int:
    count = 1
    aux = numero
    while count <= aux:
		numero*= count
        count += 1
    return numero