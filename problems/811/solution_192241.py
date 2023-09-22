def colchao(medidas,H,L):
    """Retorna um valor bool caso Joao consiga
    passar com um colchao por uma porta dados as
    dimensoes do colchao e a altura e a largura
    da porta.
    list, int, int -> bool"""
    altura_colchao = medidas[0]
    largura_colchao = medidas[1]
    comprimento_colchao = medidas[2]
    if (((largura_colchao > H) and (largura_colchao > L)) and ((comprimento_colchao > H) and (comprimento_colchao > L))) == True:
        return False
    else:
        return True