def filtra_pares(i):
    ''' Função que dada uma tupla (i) que contenha 4 elementos
    inteiros retorna apenas os elementos pares
    Entrada: tupla (int,int,int,int)
    Retorno: tupla (*) *o número de elementos é igual ao número de elementos pares '''
    
    resto_elem1 = i[0]%2
    resto_elem2 = i[1]%2     
    resto_elem3 = i[2]%2
    resto_elem4 = i[3]%2

    if resto_elem1==0 and resto_elem2==0 and resto_elem3==0 and resto_elem4==0:
        return i[0],i[1],i[2],i[3]

    elif resto_elem1==0 and resto_elem2==0 and resto_elem3==0:
        return i[0],i[1],i[2]

    else:
        if resto_elem1==0 and resto_elem2==0:
            return i[0],i[1]

        elif resto_elem1==0 and resto_elem3==0:
            return i[0],i[2]

        else:
            if resto_elem1==0 and resto_elem3==0 and resto_elem4==0:
                return i[0],i[2],i[3]

            elif resto_elem1==0 and resto_elem4==0:
                return i[0],i[3]

            else:
                if resto_elem1==0:
                    return i[0]

                elif resto_elem2==0 and resto_elem3==0 and resto_elem4==0:
                    return i[1],i[2],i[3]

                else:
                    if resto_elem2==0 and resto_elem3==0:
                        return i[1],i[2]

                    elif resto_elem2==0 and resto_elem4==0:
                        return i[1],i[3]

                    else:
                        if resto_elem2==0:
                            return i[1]

                        elif resto_elem3==0 and resto_elem4==0:
                            return i[2],i[3]

                        else:
                            if resto_elem3==0:
                                return i[2]

                            elif resto_elem4==0:
                                return i[3]

                            else:
                                return ()