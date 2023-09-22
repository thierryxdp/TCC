def insere(lista_numero, n):
    """A função recebe como entrada uma lista ordenada de números
    e um inteiro n, e retorna a lista recebida, porém com o elemento
    n adicionado na posição de ordem da lista."""
    lista_numero.append(n)
  
    return list.sort(lista_numero)