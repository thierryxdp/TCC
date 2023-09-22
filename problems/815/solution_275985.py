def insere(lista_numero, n):
    """Esta função acrescenta um nýmero N em uma lista de números, de forma crescente.
    assinatura list,int -> list 
    """
    list(lista_numero)
    lista_numero.append(n)
    return sorted(lista_numero)