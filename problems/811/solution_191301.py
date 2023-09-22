def passa_colchao(colchao,H,L):
    """Função que dado as dimensões de um colchão e a altura e largura de uma porta, retorna se é possível ou não
o colchão passar pela porta.
list, float, float --> bool
testes:
passa_colchao([25,120,220], 200, 100) == True
passa_colchao([25,205,220]), 200, 100 == False
passa_colchao([25,200,220]), 200, 100 == True
As medidas em ordem crescente de tamanho (A,B,C) foram feitas para o colchão em pé
    A = comprimento
    B = largura
    C = altura
    H = altura da porta
    L = largura da porta
    
"""
    if colchao[1]<=H and colchao[0]<=L:
        return "True"
    else:
        return "False"