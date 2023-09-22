def maiores(lista_numeros,n):
    """Está função retorna uma nova lista com os números maiores que 'n'
    na lista 'lista_numeros'"""
    list.sort(lista_numeros);
    t=len(lista_numeros)
    if n>lista_numeros[0] and t>1:
        if n>lista_numeros[1] and t>2:
            if n>lista_numeros[2] and t>3:
                if n>lista_numeros[3] and t>4:
                    if n>lista_numeros[4] and t>5:
                        if n>lista_numeros[5] and t>6:
                            if n>lista_numeros[6] and t>7:
                                if n>lista_numeros[7] and t>8:
                                    if n>lista_numeros[8] and t>9:
                                        new=[]
                                        return []
                                    else: 
                                        return lista_numeros[8:]
                                else:
                                    return lista_numeros[7:]
                            else:
                                return lista_numeros[6:]
                        else:
                            return lista_numeros[5:]
                    else:
                        return lista_numeros[4:]
                else:
                    return lista_numeros[3:]
            else:
                return lista_numeros[2:]
        else:
            return lista_numeros[1:]
    else:
		return lista_numeros[0:]