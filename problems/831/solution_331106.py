def lingua_p(palavra):
    vogal='AEIOUÁÉÍÓÚaeiouáéíóú'
    nova_palavra=[]
    for letra in list(palavra):
        if letra in vogal:
            nova_palavra += letra+'p'+letra
        else:
            nova_palavra.append(letra)
    return .join(nova_palavra)