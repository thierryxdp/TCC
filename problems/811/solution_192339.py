def colchao(medidas,H,L):
    """string int int -> tupla int int"""
     """O procedimento colchão irá retornar True ou False,
    caso a largura ou o comprimento do colchão maior ou menor que
    a altura ou largura da porta.
    
    Como uma lista retorna valores em string, o método int()
    converte esse valor para inteiro, fazendo assim o procedimento
    funcionar corretamente"""
    if int(medidas[1])<=H or int(medidas[2])<=L: 
        return True
    else:
        return False