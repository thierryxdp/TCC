def posLetra( nome, letra, n):
    ''' retorna a posição em que está a ocorrência da string; 
    entrada -> string, letra, ocorrencia; str, str, int -> int'''
    i=0
    qtd_letra =0

    while i < len(nome):
      	if letra == nome[i]:
        	qtd_letra = qtd_letra +1 
      	i = i +1
    if qtd_letra < n:
     	return -1
    else:
      	return (nome.find(letra,n))