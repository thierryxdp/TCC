def busca(setor,matriz):
    """funcao que retorna os dados de um funcionario buscado atraves de seu setor;
    str,list(list) -> list(list)"""

    found_setor = []

    for i in range(len(matriz)) :

        if setor in matriz[i][2]:
            funci = matriz[i]
            del funci[2]
            found_setor.append(funci)
          

    return found_setor