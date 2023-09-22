#Start your python function def pares(numeros):

def filtra_umpares (numeros):
    ''' funcao que dado 4 numeros retorna os numeros pares
          parametros: numeros=numeros dados pelo usuario
               tuple -> tuple '''
    tuplavazia = ()

	if (int(numeros[0]) % 2) == 0:
		tuplavazia = tuplavazia + (numeros[0],)
	if (int(numeros[1]) % 2) == 0:
		tuplavazia = tuplavazia + (numeros[1],)
	if (int(numeros[2]) % 2) == 0:
		tuplavazia = tuplavazia + (numeros[2],)
	if (int(numeros[3]) % 2) == 0:
		tuplavazia = tuplavazia + (numeros[3],)

	return tuplavazia

valorRecebidoPeloUsuario = tuple(x.strip() for x in input('digite 4 numeros separados por virgula (,):').split(','))

print(pares(valorRecebidoPeloUsuario))