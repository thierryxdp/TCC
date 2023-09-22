def lingua_p(palavra):
    vogal= 'aeiouAEIOUáéíóúÁÉÍÓÚ'
    aux=''
    for letra in palavra:
        aux = aux+letra
        if letra in vogal:
            aux=aux+('p'+letra)  
    return aux.lower()