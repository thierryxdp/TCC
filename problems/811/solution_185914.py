# Dadas uma lista com as medidas de um colchão em ordem
# crescente e a altura e largura das portas, respectivamente,
# queremos saber se o colchão pode passar pelas portas.
# list, float, float -> bool
# Resolução:
# 1. Como as medidas estão em ordem crescente, basta analisar
#    se as duas menores são simultaneamente menores ou iguais
#    às dimensões da porta;
# 1.1 Se a menor medida e a segunda menor medida são respectivamente
#     menores ou iguais à altura e à largura da porta, retorna True;
# 1.2 Se a menor medida e a segunda menor medida são respectivamente
#     menores ou iguais à largura e à altura da porta, retorna True;
# 1.3 Se essas condições não são cumpridas, retorna False.

def colchao(medidas, H, L):
    '''Dadas uma lista com as medidas de um colchão em ordem
    crescente e a altura e largura das portas, respectivamente,
    devolve True se o colchão pode passar e False se não;
    list, float, float -> bool'''
    if (medidas[0] <= H) and (medidas[1] <= L):
        return 1 == 1
    if (medidas[0] <= L) and (medidas[1] <= H):
        return 1 == 1
    else:
        return 0 ==  1