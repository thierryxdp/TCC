def filtra_pares(elementos):
	if not verifica(elementos):
        raise erro("separa: argumentoi incorreto")
        
        menores = tuple (it for it in elementos if it[1] < 18)
        maiores = tuple (it for it in elementos if it[1] >= 18)
        return (menore, maiores)