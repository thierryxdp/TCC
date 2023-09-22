def busca(setor,mtz):
    ''' Retorna os dados dos funcionários do setor pedido
    lista,string->lista'''
    escolhidos=[]
    for linha in mtz:
        if linha[2]==setor:
            linha.remove(setor)
            escolhidos+=[linha]
    return escolhidos