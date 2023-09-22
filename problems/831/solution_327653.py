def lingua_p(palavra):
    cont=0
    palavraseparada=list(palavra)
    for i in palavra:
        if i in 'AEIOUaeiou':
            palavraseparada[cont]=i+'p'+i
        cont=cont+1
    return str.join('',palavraseparada)