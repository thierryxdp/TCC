def uppCons(lista):
        """
        """
        lista_nova = lista
        for i in (lista):
            if i in not "aeiou":
                lista_nova = lista_nova.upper(i)
                lista_nova = lista_nova.replace(lista, lista_nova)
            return lista_nova