def insere(lista_numerica,numero):
    """Recebe uma lista de números inteiros e um número inteiro, adiciona o número na lista
       e retorna essa nova lista ordenada em ordem crescente.
       list, int-> list

       Parameters:
       lista_numerica: Uma lista de números inteiros.
       numero: O número inteiro que será adicionado na lista."""
    lista2=lista_numerica+[numero]
    list.sort(lista2)
    return lista2