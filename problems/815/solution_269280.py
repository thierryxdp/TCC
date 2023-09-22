def insere(lista_numero, n):
    """
       list,int->list
       :param lista_numero: Recebe lista com numeros crescentes inteiros
       :param n: Um numero inteiro qualquer
       :return: Adiciona o numero n na lista de forma que ela continue crescente
       """
    lista_numero.append(n) 
    lista_numero.sort() 
    return lista_numero