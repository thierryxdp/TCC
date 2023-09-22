def filtragem(t):
    ''' Função que retorna uma nova tupla contendo apenas elementos pares da tupla original'''
    nova_tupla = ()
    if t[0] % 2 == 0:
        nova_tupla = nova_tupla + (t[0],)
	if t[1] % 2 == 0:
		nova_tupla = nova_tupla + (t[1],)
    if t[2] % 2 == 0:
        nova_tupla = nova_tupla + (t[2],)
	if t[3] % 2 == 0:
		nova_tupla = nova_tupla + (t[3],)
	return nova_tupla