def insere(lista_numero,n):
    """A função recebe como parâmetro uma lista ordenada 
    crescente de números inteiros, e um número inteiro 'n'.
    Ela retornará 'n' dentro da lista ordenada crescente,
    respeitando a sequência estabelecida.
    
    Entrada: List, Int
    Saída: List"""
    
    lista = list(lista_numero)
    list.append(lista,n)
    list.sort(lista)
    return lista