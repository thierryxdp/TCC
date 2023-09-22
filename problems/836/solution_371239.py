def busca(setor,lista):
    def verifica(lista):
        return True if setor in lista else False
    return list(filter(verifica,lista))