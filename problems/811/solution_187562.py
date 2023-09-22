def colchao(dimensoes_colchao,H,l)
'''funcao que, dadas as dimensoes do colchao em ordem crescente, a altura e a largura da
porta, respectivamente, em centimetros, retorna se o colchao passa ou nao pela porta com
uma de suas faces paralelas ao chao; (list(int,int,int),int,int)-> bool'''
    dim_maior=dimensoes_colchao[2]
    dim_media=dimensoes_colchao[1]
    dim_menor=dimensoes_colchao[0]
    if dim_maior<=H and dim_media<=L:
        return 'True'
    elif dim_maior>H and dim_media<=H:
        return 'True'
    else:
        return 'False'