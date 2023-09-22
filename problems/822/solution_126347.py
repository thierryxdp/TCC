def repetidos(numeros):
        valor = 0
        i = 1
        while i < len(numeros):
            if numeros[i] == numeros[i - 1]:
                valor = valor + 1
            i = i + 1
        return valor