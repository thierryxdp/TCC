def faltante(lista):
    
	contador=0
	soma=0

    while contador <= len(lista):
        soma = soma + (lista[contador]-1)
        contador = contador + 1
        
	return soma