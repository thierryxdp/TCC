def conta_frases(texto:str)->int:
    A = list(filter(('').__ne__, texto.split('...')))
	B = list(filter(('').__ne__, texto.split('.')))
	C = list(filter(('').__ne__, texto.split('!')))
	D = list(filter(('').__ne__, texto.split('?')))
	return len(A) + (0**len(A)-1) + len(B) + (0**len(B)-1) + len(C) + (0**len(C)-1) + len(D) + (0**len(D)-1)