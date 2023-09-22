def busca(setor, matriz):
    '''Função que recebe uma string que representa o setor de uma 
    	empresa e uma matriz em que o primeiro item é o nome do
        funcionário, o segundo o registro, o terceiro o setor e o
        quarto o telefone e retorna os dados das pessoas que 
        trabalham nesse setor passado como parâmetro
        
        int, list(list(str)) -> list(list(str))''''
    
    resultado = []
    for linha in matriz:
        if setor in linha:
            list.remove(linha, setor)
            resultado = resultado + linha
    return resultado