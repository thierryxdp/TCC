def bolos(quantidade_farinha, quantidade_ovo, quantidade_leite):
    bolo = 0
	while quantidade_farinha >= 2 and quantidade_ovo >= 3 and quantidade_leite>= 5:
  bolo = bolo + 1
  quantidade_farinha = quantidade_farinha - 2
  quantidade_ovo = quantidade_ovo - 3
  quantidade_leite = quantidade_leite - 5
    return bolo