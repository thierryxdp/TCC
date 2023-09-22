def uppCons(lista):
        """
        """
        lista_nova = lista
        for i in (lista):
            if i in "aeiou":
                lista_nova = lista_nova.replace(lista[i], lista_nova.upper())
            return lista_nova