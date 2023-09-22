def uppCons(lista):
        """
        """
        lista_nova = lista
        for i in (lista):
            if i not in "aeiou":
                lista_nova = lista_nova.replace(lista.upper(), lista_nova)
            return lista_nova