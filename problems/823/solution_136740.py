def faltante(lista, nome):
    """Busca um usuário a partir do seu nome registrado e adiciona em uma nova lista de contatos.
    list,str -> list """
    contatos = []
    contador = 0
    while contador < len(lista):
        if nome.lower() in lista[contador][0].lower():
            contatos.append(lista[contador])
        contador += 1
    return contatos