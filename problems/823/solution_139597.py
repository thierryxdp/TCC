def faltante(lista_pecas):
    """função que dada uma lista com N-1 inteiros numerados de 1 a N, descobre qual número inteiro está  faltando
    lista -> int"""
        i = 1
        while i < len(lista_pecas):
            if i not in lista_pecas:
                return 
            contador += 1
        return lista_pecas