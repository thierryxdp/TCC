def melhor_volta(m):
    """A função retorna uma tupla com 3 valores: o corredor que teve a melhor volta,
       o tempo da menor volta e essa volta.
       lista -> tupla
       Explicação: 1o criamos uma lista para guardar a menor volta de cada corredor;
       2o: comparamos o valor mínimo da lista criada com cada valor da matriz parâmetro,
       assim conseguiremos saber quem teve essa volta.
       3o: retornamos a tupla pedida.
       obs.: Os índices vão de 0 a 5, mas os corredores são identificados de 1 a 6,
       logo, ao retornar os índices na tupla, devemos somar 1."""
    minimos = []
    i = 0
    while i < len(m):
        list.append(minimos, min(m[i]))
        i = i+1
    for k in range(len(m)):
         for j in range(len(m[0])):
            if min(minimos) == m[k][j]:
                return k+1, m[k][j], j+1
#Teste:
#m = [[12, 15, 18, 29, 30, 25, 40, 27, 43, 30], [23, 21, 19, 32, 24, 22, 41, 26, 20, 9], [33, 14, 11, 10, 45, 8, 29, 28, 31, 36], [34, 6, 17, 35, 46, 7, 42, 13, 37, 16], [44, 55, 73, 60, 88, 47, 53, 72, 52, 64], [69, 59, 62, 50, 78, 49, 51, 70, 47, 61]]
#melhor_volta(m)--> (4, 6, 2)