# Dada uma lista com peças de comprimento N-1, com peças de 1 a N (não 
# necessariamente ordenada), esta função retorna o número inteiro x pertencente
# ao intervalo [0,N] que está faltando.
# list -> list

def faltante(lista):
    padrao = list(range(1,len(lista)+2,1))
    i=0
    
    while i<=len(padrao):
    	if padrao[i] not in lista:
            return i+1
        i= i +1