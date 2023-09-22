def lingua_p(palavra):
    cont=0
    for i in palavra:
        if i in 'AEIOUaeiou':
            palavra[cont:cont]='teste'