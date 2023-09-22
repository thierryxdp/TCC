def bolos(A, B, C):
    """ Computa a quantidade máxima possível de bolos
    que demandam os ingredientes abaixo, dados as
    quantidades disponíveis indicadas por A, B e C.
    A := xícaras
   	B := ovos
   	C := colheres
   	1 bolo requer 2A + 3B + 5C
   
   	Casos de teste:
   	bolos(0, 10, 40) == 0
    bolos(10, 0, 90) == 0
    bolos(8, 67, 0) == 0
    bolos(4, 6, 10) == 2"""
	return min(A//2, B//3, C//5)