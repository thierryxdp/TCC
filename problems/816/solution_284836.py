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
                        new_list=[lista_numeros[4:-1]]
                        return new_list
                else:
                    new_list=[lista_numeros[3:-1]]
                    return new_list
            else:
                new_list=[lista_numeros[2:-1]]
                return new_list
        else:
            new_list=[lista_numeros[1:-1]]
            return new_list
    else:
        new_list=[lista_numeros[0:-1]]
        return new_list