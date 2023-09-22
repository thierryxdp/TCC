def melhor_volta(m):
    """função que recebe um matriz (m) de tamanho 6x10, ou seja, de
    colunas e linhas, na qual as colunas correspondem as voltas e as
    linhas ao número do jogador. E analisa qual a melhor volta dentre
    os corredores, de modo que analise cada tempo de cada jogador. E
    que deve retornar um tupla, que contenha o corredor, a melhor volta
    e em qual volta foi o melhor;
    matriz->tupla"""
    linhas = range(len(m))
    colunas = range(len(m[0]))
    melhores = []
    volta = 1
    for i in linhas:
        minimo = min(m[i])
        list.append(melhores,minimo)
    melhor = min(melhores)
    corredor = list.index(melhores,melhor)+1
    for i in linhas:
        for j in colunas:
            if m[i][j]==melhor:
                volta = volta+j
    return corredor, melhor, volta