def busca(matriz,setor):
    contato=[]
    for i in range(len(matriz)):
        if setor==matriz[i][2]:
            contato=matriz[i]
            del contato[i:2]
            if telefone not in contatos[i][2]:
                return []
    return contato