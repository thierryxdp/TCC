def faltante(lista_pecas):
        i = 1
        while i < len(lista_pecas):
            if i not in lista_pecas:
                return 
            i += 1
        return i