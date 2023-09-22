def bolos(farinha, ovo, leite):
    receita = ((farinha / 2) + (ovo / 3) + (leite / 5)) // 3
    if (farinha  / 2) < 1 or (ovo / 3) < 1 or (leite / 5) < 1:
            return 0
    else:
           	return  int((receita))