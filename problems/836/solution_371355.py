def busca(setor, matriz):
    """Dada uma matriz dos funcionários de uma empresa com 4 entradas 
    (nome,registro,setor e telefone) como parâmetro, a função vai retornar
    os dados dos funcionários daquele determinado setor, dado também como parâmetro
    para busca na matriz empresárial.
       O setor deve ser escrito entre aspas e a matriz deve ser escrita entre colchetes[], 
       com cada linha da matriz sendo representada dentro de um colchetes também;
       str, matriz(lista de listas) --> matriz(lista de listas)"""
    resultado = []
    for linha in range(len(matriz)):
        for elemento in range(len(matriz[0])):
            if matriz[linha][elemento] == setor:
                list.append(resultado, (matriz[linha]))
        if (matriz[linha])[2] == setor:
            list.remove((matriz[linha]), setor)
    return resultado