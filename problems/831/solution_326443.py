def lingua_p(palavra):
    
    resultado = []
    
    for letra in palavra:
        if letra in 'AEIOUaeiouáéíóúàèìòùâôã':
            resultado.append(letra + 'p' + letra)
        
        else:
            resultado.append(letra)
            
    resultado = ''.join(resultado)
    return resultado