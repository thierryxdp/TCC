def lingua_p(palavra):
    cont=0
    palavraseparada=list(palavra)
    for i in palavra:
        if i in 'AEIOUaeiou':
            palavraseparada[cont]='ap'
            return palavraseparada