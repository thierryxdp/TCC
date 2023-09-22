def madia_matriz (matriz):
    """funçao que recebe uma matriz no formato lista de listas de inteiros nao vazia e retorna a media de todos os numeros da matriz;
    entrada: list;
    saida: float."""
    
    nums = []
    for linhas in matriz:
        for colunas in linhas:
            nums = nums + [colunas]
    
    total = sum(nums) / len (nums)
    
    return round (total,2)