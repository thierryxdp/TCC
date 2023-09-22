def lingua_p(palavra):
    ''' funcao que recebe uma stirns e retona a mesma strin porem onde a vogais troca-se por a mesma vogal +p + mesma vogal: str->str'''
    a=''
    for i in range(len(palavra)):
        if palavra[i] in 'ÁÉÚAEIOUáéúaeiou':
            a+=palavra[i].replace(palavra[i],palavra[i]+'p'+palavra[i])
        else:
            a+= palavra[i]
    return a