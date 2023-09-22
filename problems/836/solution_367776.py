def busca (setor, matriz):
    """funçao que recebe uma matriz com o quadro de funcionarios, uma string com um setor especifico e retorna os dados dos funcionarios desse setor;
    entrada: str, list;
    saida: list."""
    funcionarios = []
    for linha in matriz:
        if linha [2] in setor:
            del (linha [2])
            funcionarios = funcionarios + [linha]
    return funcionarios