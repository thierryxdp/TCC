def filtraMultiplos(numeros: turple[], x)
resposta = list()
  for valor in numeros:
        if valor % x == 0:
            resposta.append(valor)
            return resposta