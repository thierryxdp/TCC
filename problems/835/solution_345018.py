def melhor_volta(matriz):
    '''Função que recebe uma matriz com os tempos dos corredores e retorna um tupla com a melhor volta e o corredor que a executou.
       matriz --> tupla'''
    sua_melhor_volta = []
    for jogador in matriz:
        list.append(sua_melhor_volta,min(jogador))
    b = min(sua_melhor_volta)
    a = list.index(sua_melhor_volta, b)
    c = list.index(matriz[a],b)
    return (a + 1, b, c + 1)