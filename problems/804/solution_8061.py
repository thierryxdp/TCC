def filtra_pares(valorRecebidoPeloUsuario):
    
    '''Funcao que retorna uma tupla contendo elementos pares da tupla original
    		Parametros: valores digitados pelo usuario
            	tuple -> tuple '''

		tupla = ();
		if (valorRecebidoPeloUsuario[0] % 2) == 0:
			tupla = (valorRecebidoPeloUsuario[0])

		if (valorRecebidoPeloUsuario[1] % 2) == 0:
		    tupla = (tupla, valorRecebidoPeloUsuario[1])

		if (valorRecebidoPeloUsuario[2] % 2) == 0:
		    tupla = (tupla, valorRecebidoPeloUsuario[2])

		if (valorRecebidoPeloUsuario[3] % 2) == 0:
		    tupla = (tupla, valorRecebidoPeloUsuario[3])

		return tupla

valorRecebidoPeloUsuario = tuple(int(x.strip()) for x in input('digite 4 numeros separados por virgula (,):').split(','))

print(filtra_pares(valorRecebidoPeloUsuario))#Start your python function here