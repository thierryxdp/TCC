def busca(m,setor):
    "Funcao que retorna lista de funcionarios de um setor"
    n=[]
    for i in range(len(m)):
        if m[i][2] == setor:
            return m[i][0],m[i][1]