def faltante (lista):
    """Função que, dada uma lista com numero inteiros, retonar o numero na lista da peça que está faltando.
    Entrada: lista[int].
    Saída: int."""
    
    list.sort(lista)
    i = 0
    
    x = list(range(1,len(lista)+2))
    y = list(range(1,len(lista)+1))
    
    if lista == y:
        return lista[len(lista)-1]+1
    else:
        while lista[i] == x[i]:
            i = i+1
        return x[i]