def posLetra(frase, letra, n):
    lista = []
    
    if letra in frase:
        for i in frase:
            if i == letra:
                lista.append(frase.index(i))
        
        return lista[n - 1]
        
    else:
        return -1