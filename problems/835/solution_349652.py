def melhor_volta(Matriz):
    '''Função que dada uma matriz, retorna a volta mais rapida,
    quem a  fez e em qual foi o numero desta volta: list -> tuple'''
    lista = []
    menor = []
    minimo = 0
    ContadorLinhas = 0
    ContadorColunas = 0
    for menor in Matriz:
        lista += [min(menor)]
    minimo = min(lista)
    for linhas in Matriz:
        ContadorLinhas += 1
        if minimo in linhas:
            for colunas in linhas:
                ContadorColunas += 1
                if colunas == minimo:
                    break
            return (ContadorLinhas, minimo, ContadorColunas)