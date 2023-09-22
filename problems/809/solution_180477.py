def intercala(lista1,lista2):
    ''' funcao que intercala duas listas de tamanho 3 gerando uma lista de tamanho 6
        list[a,b,c],list[c,d,e] --> list[a,b,c,d,e,f] '''
    return lista1[:1] + lista2[:1] + lista1[1:2] + lista2[1:2] + lista1[2:] + lista2[2:]