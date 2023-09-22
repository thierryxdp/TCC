def lingua_p(palavra):
    'recebe uma palavra e retorna essa palavra com um p em seguida de cada vogal'
    vogal= 'aeiouAEIOUáéíóúÁÉÍÓÚ'
    aux=''
    for letra in palavra:
        aux = aux+letra
        if letra in vogal:
            aux=aux+('p'+letra)  
    return aux.lower()