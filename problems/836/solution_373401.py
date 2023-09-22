def busca(setor,matriz):
    """Dadaos um setor e uma matriz, retorna os dados
    das pessoas desse setor.
    str, list -> list"""   
    lista=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if setor == matriz[i][j]:
                linha=[]
                pessoa = matriz[i][j-2]
                linha.append(pessoa)
                registro = matriz[i][j-1]
                linha.append(registro)
                telefone = matriz[i][j+1]
                linha.append(telefone)
        		lista.append(linha)   
    return lista