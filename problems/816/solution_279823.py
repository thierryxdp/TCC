def maiores(listaNum):
    """funcao que retorna todos os numeros de uma determinada lista maiores que determinado numero n"""
    copiaLista=listaNum[:4:]
    copiaLista.sort()
    return copiaLista[+1]