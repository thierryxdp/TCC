def primo(numero):
    """Verfica se o numero é primo ou não.
    Parametros:
    Entrada:int
    Saida:booleano"""
 	contador=0
    for indice in range(1,numero+1):
        if numero%indice==0:
        	contador=contador+1
    if contador==2:
        return True
	return False