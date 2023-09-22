def busca(matriz, setor):
    '''Função que recebe uma matriz (cujas linhas apresentam o
    	o formato: primeiro item representa o nome, o segundo
        o registro, o terceiro o setor e o quarto o telefone) e
        um setor e retorna os dados das pessoas que trabalham nesse
        setor passado como parâmetro
        
        list(list(str)), int -> list(list(str))''''
    
    resultado = []
    for linha in matriz:
        if setor in linha:
            list.remove(linha, setor)
            resultado = resultado + linha
    return resultado