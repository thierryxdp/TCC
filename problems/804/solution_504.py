def filtra_pares(tupla):
	'''Função que recebe uma tupla com quatro elementos inteiros como parâmetro 
	e retorna uma nova tupla contendo apenas os elementos pares da tupla original, mantendo a ordem;
	Entrada: tupla
	Saída: tupla'''
	tupla0=tupla[0]%2
	tupla1=tupla[1]%2
	tupla2=tupla[2]%2
	tupla3=tupla[3]%2
	if tupla0!=0 and tupla1!=0 and tupla2!=0 and tupla3!=0:
		return ()
	elif tupla0!=0 and tupla1==0 and tupla2==0 and tupla3==0:
		return (tupla[1],tupla[2],tupla[3])
	elif tupla0==0 and tupla1!=0 and tupla2==0 and tupla3==0:
		return (tupla[0],tupla[2],tupla[3])
	elif tupla0==0 and tupla1==0 and tupla2!=0 and tupla3==0:
		return (tupla[0],tupla[1],tupla[3])
	elif tupla0==0 and tupla1==0 and tupla2==0 and tupla3!=0:
		return (tupla[0],tupla[1],tupla[2])
	elif tupla0==0 and tupla1==0 and tupla!=0 and tupla3!=0:
		return (tupla[0],tupla[1])
	elif tupla0==0 and tupla1!=0 and tupla2==0 and tupla3!=0:
		return (tupla[0],tupla[2])
	elif tupla0==0 and tupla1!=0 and tupla2!=0 and tupla3==0:
		return (tupla[0],tupla[3])
	elif tupla0!=0 and tupla1==0 and tupla2==0 and tupla3!=0:
		return (tupla[1],tupla[2])
	elif tupla0==0 and tupla1!=0 and tupla2!=0 and tupla3!=0:
		return (tupla[0])
	elif tupla0!=0 and tupla1==0 and tupla2!=0 and tupla3!=0:
		return (tupla[1])
	elif tupla0!=0 and tupla1!=0 and tupla2==0 and tupla3!=0:
		return (tupla[2])
	elif tupla0!=0 and tupla1!=0 and tupla2!=0 and tupla3==0:
		return (tupla[3],)
	elif tupla0!=0 and tupla1!=0 and tupla2==0 and tupla3==0:
		return (tupla[2],tupla[3])
	else:
		return (tupla[0],tupla[1],tupla[2],tupla[3])