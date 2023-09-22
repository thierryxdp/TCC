def insere(lista_numero, n):
    """Função que dada uma lista ordenada de números inteiros e um número inteiro n, inclui n na lista de modo que ela continue crescente.
    list -> list """

    if n >= 0 and n < 10:
        n_str = str(n)
        n_lista = list(n_str)

        lista = lista_numero + n_lista
        lista[-1] = int(n_str)

        list.sort(lista)
        
        return lista

    if n >= 10 and n < 100:

        n_str = str(n)
        n_lista = list(n_str)

        n_lista[0] = n_lista[0] + n_lista[1]
        del(n_lista[1])
        
        lista = lista_numero + n_lista
        lista[-1] = int(n_str)

        list.sort(lista)
        
        return lista


    if n >= 100 and n < 1000:

        n_str = str(n)
        n_lista = list(n_str)

        n_lista[0] = n_lista[0] + n_lista[1] + n_lista[2]
        del(n_lista[1])
        del(n_lista[1])
        
        lista = lista_numero + n_lista
        lista[-1] = int(n_str)

        list.sort(lista)
        
        return lista

    if n < 0 and n < 10:

        n_str = str(n)
        n_lista = list(n_str)

        n_lista[0] = n_lista[0] + n_lista[1]
        del(n_lista[1])
        
        lista = lista_numero + n_lista
        lista[-1] = int(n_str)

        list.sort(lista)
        
        return lista



#Podemos continuar criando a função para casos maiores e rapidamente estaríamos na casa dos milhões.