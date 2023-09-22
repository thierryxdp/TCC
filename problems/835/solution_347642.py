def melhor_volta(m):
    """função que recebe um matriz (m) de tamanho 6x10, ou seja, de
    colunas e linhas, na qual as colunas correspondem as voltas e as
    linhas ao número do jogador. E analisa qual a melhor volta dentre
    os corredores, de modo que analise cada tempo de cada jogador. E
    que deve retornar um tupla, que contenha o corredor, a melhor volta
    e em qual volta foi o melhor;
    matriz->tupla"""
    linhas = range(len(m))
    menor = []
    volta = 1
    for i in linhas:
        minimo = min(m[i])
        list.append(menor,minimo)
        colunas = range(len(m[0]))
        melhor_tempo = min(menor)
        for j in colunas:
            if m[i][j]!=melhor_tempo:
                volta = volta + 1
    corredor = list.index(menor,melhor_tempo)+1
    return corredor,melhor_tempo,volta