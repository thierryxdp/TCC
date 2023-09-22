def inverte(frase):
    
    a = str.join(' ', str.split(frase, '.'))
    b = str.join(' ', str.split(a, ','))
    c = str.join(' ', str.split(b, '?'))
    d = str.join(' ', str.split(c, '!'))
    e = str.join(' ', str.split(d, '-'))
	minusculo     = e.lower().strip()
	separar       = str.split(sem_pontuacao," ")
	inverter      = separar[::-1]
    
 	return inverter