def faltante(lista):
    
	contador=0
	soma=0

    while contador <= len(lista)-1:
        soma = soma + lista[contador]
        contador = contador + 1
        
	return soma