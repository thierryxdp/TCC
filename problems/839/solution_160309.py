def carros(pessoas,capacidade=5):
  		if capacidade> pessoas*2+1:
            return int(pessoas/capacidade)+1
        else:
        return int(pessoas/capacidade)