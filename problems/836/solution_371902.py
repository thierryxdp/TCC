def busca(setor,matriz):
    "recebe um setor e uma matriz com nome,registro,setor,numero"
    "então faz uma busca dos funcionarios do setor e retorna as informações destes"
    "entrada:str. saida:str"
    linhas=len(matriz)
    coluna=len(matriz[0])
    lista=[]
    x=0
    while x<linhas:
        if setor==matriz[x][2]:
            lista=lista+[matriz[x][0]]
        else:
            lista=lista
        x==x+1
        return lista