def uppCons(lista):
        """
        """
        lista_nova = lista
        for i in (lista):
            if i not in "aeiou":
                lista_nova = lista_nova.upper()
                lista_nova = lista_nova.replace(lista, lista_nova)
            return lista_nova