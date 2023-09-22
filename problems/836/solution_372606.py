def busca(setor, matriz):
    """Dada uma frase que representa um setor, e uma matriz com
    informações pessoais, a função irá retornar as informações pessoais
    das pessoas que trabalham naquele setor, com exceção desta informação.
    Tipo da variável frase: str
    Tipo da variável matriz: list
    Tipo da saída: list"""
    linha = len(matriz)
    lista = []
    elemento = 0
    for i in range(linha):
        if setor in matriz[i]:
            list.append(lista,matriz[i])
            list.remove(lista[elemento],setor)
            elemento += 1
    return lista