def colchao(lista_medidas):
    '''Função que retorna se é possível passar um colchão pela porta da casa do
    comprador. Os parâmetros as medidas de largura, comprimento e altura do retângulo,
    respectivamente e as medidas de altura e largura da porta. Lista--> boolean'''
    medidas_colchao=lista_medidas[0]
    lagura= medidas_colchao[0]
    comprimento= medidas_colchao[1]
    altura= medidas_colchao[2]
    #com a face da altura paralela ao chão
    if((comprimento<=lista_medidas[2] or comprimento<=lista_medidas[1])):
        return True
    elif(altura<=lista_medidas[1] or altura<=lista_medidas[2]): #com a face do comprimento X largura paralela
        return True
    else:
        return False