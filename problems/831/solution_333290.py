'''Resolução com While'''
def lingua_p(palavra):
    traduzido_p = []
    contador = 0
    limite = len(palavra)
    
    while contador < limite:
        if palavra[contador] in 'aeiouáéíóú':
            traduzido_p.append(palavra[contador] + 'p' + palavra[contador])
        else:
            traduzido_p.append(palavra[contador])
        contador += 1
    return ''.join(traduzido_p)