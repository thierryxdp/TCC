def faltante(lista):
    """
    Função que recebe uma lista de N inteiros de 1 até N+1
    e retorna o número que falta para completar a lista
    """
    if len(lista)==1:
        return 1+(lista[0]==1)
    if lista[0]==1:
        i=0
        while i < len(lista)-1:
            if (lista[i+1]-lista[i])!=1:
                return lista[i]+1
            i+=1
        return len(lista)+1
    return 1