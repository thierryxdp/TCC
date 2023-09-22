def busca(setor, matriz):
    """
    Código que busca dados do funcionário compativeis com o 
    setor fornecido da matriz
    :setor --> str:
    :matriz --> list:
    :return --> list:
   
    """
   
    banco_dados= []
    
    for i in range(len(matriz)):
        if setor in matriz[i]:
            banco_dados.append(matriz[i])
    
    
    for j in range(len(banco_dados)):
        if banco_dados[j][2] == setor:
            del banco_dados[j][2]
    if banco_dados == []:
        banco_dados = 'Nenhum registro encontrado'
    return banco_dados