def maiores(lista_numeros,n):
    """Está função retorna uma nova lista com os números maiores que 'n'
    na lista 'lista_numeros'"""
    list.sort(lista_numeros);
    if n>lista_numeros[0]:
        if n>lista_numeros[1]:
            if n>lista_numeros[2]:
                if n>lista_numeros[3]:
                    if n>lista_numeros[4]:
                        new_list=[]
                        return new_list
                    else:
                        return lista_numeros[4:]
                else:
                    return lista_numeros[3:]
            else:
                return lista_numeros[2:]
        else:
            return lista_numeros[1:]
    else:
        return lista_numeros[]