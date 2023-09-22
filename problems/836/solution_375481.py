def busca(setor,matriz):
    'retorna lista com os funcionarios encontrados na matriz de um setor;lista,string--lista'
    i=0
    funcionarios=[]
    while i<len(matriz):
        if matriz[i][2]==setor:
            nome=matriz[i][0]
            registro=matriz[i][1]
            telefone=matriz[i][3]
            funcionarios+=[[nome,registro,telefone],]
         i+=1
        return funcionarios