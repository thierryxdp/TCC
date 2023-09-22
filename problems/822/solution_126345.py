def repetidos(numeros):
      '''Dado uma lista, a função retornará o numero de vezes que um numero foi igual ao anterior.'''
        valor=0
        i = 1
        while i < len(numeros):
            if numeros[i] == numeros[i - 1]:
                valor = valor + 1
            i = i + 1
            return valor