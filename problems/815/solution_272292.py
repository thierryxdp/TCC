def insere(lista_numero:list,n:int)->list:
    lista_numero.append(n)#adiciona um numero qualquer no final
    list.sort(lista_numero)#reorganiza
    return lista_numero #retorno