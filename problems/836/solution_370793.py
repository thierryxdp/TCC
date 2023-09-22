def busca(nome,matriz):
    """Função que ao receber um nome e uma martriz, retorna os dados de
    do nome buscado;
    str, list -> list"""
    contato = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if nome in matriz[i][j]:
                contato.append([matriz[i][0],matriz[i][1], matriz[i][3]])             
    return contato