def passa_colchao(colchao,H,L):
    """Função que dado as dimensões de um colchão e a altura e largura de uma porta, retorna se é possível ou não
o colchão passar pela porta.
list, float, float --> bool
testes:
passa_colchao([25,120,220], 200, 100) == True
passa_colchao([25,205,220]), 200, 100 == False
passa_colchao([25,200,220]), 200, 100 == True

"""
    if colchao[1]<=H and colchao[0]<=L:
        return "True"
    else:
        return "False"