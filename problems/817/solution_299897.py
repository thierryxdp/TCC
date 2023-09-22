def maiores(lista_numeros,n):
    """Está função retorna uma nova lista com os números maiores que 'n'
    na lista 'lista_numeros'"""
    list.sort(lista_numeros);
    t=len(lista_numeros)
    if t>=1 and n>lista_numeros[0]:
        if t>=2 and n>lista_numeros[1]:
            if t>=3 and n>lista_numeros[2]:
                if t>=4 and n>lista_numeros[3]:
                    if t>=5 and n>lista_numeros[4]:
                        if t>=6 and n>lista_numeros[5]:
                            if t>=7 and n>lista_numeros[6]:
                                if t>=8 and n>lista_numeros[7]:
                                    if t>=9 and n>lista_numeros[8]:
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
    
    
def acima_da_media (notas):
    q=len(notas)
    s=sum(notas)
    m=s/q
    aprovados=maiores(notas,m)
    return aprovados