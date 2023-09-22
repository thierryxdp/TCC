#Cálculos Aplicados
#Exercício 1 - Quantos bombons pedrinho pode comprar?
def num_bombons(d : int, p : int) -> int:
    '''Essa função recebe o dinheiro que Pedrinho tem (d) e divide pelo
        preço dos bombons (p) retornando o número de bombons que ele pode
        comprar. Nenhum dos argumentos pode receber valores negativos, se
        receberem a função não funcionará corretamente.'''
    return d//p