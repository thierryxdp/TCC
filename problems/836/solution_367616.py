def busca (setor, matriz):
    """funçao que recebe uma matriz (lista de lista) com quadro de funcionarios com <nome>, <registro>, <setor>, <telefone> e uma string com um setor e retorna todos os funcionarios do setor;
    entrada: str, list;
    saida: list."""
    
    funcionarios = []
    
    for linha in matriz:
        if linha [2] in setor:
            del (linha [2])
            funcionarios = funcionarios + [linha]
    return funcionarios