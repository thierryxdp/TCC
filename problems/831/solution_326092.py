def lingua_p(palavra):
    posicao=0
    for posicao in range(len(palavra)):
        vogal=palavra[posicao]
        str.lower(palavra)
        if vogal in 'aAeEiIoOuU':
            str.replace(palavra,'a','pa')
            str.replace(palavra,'e','pe')
            str.replace(palavra,'i','pi')
            str.replace(palavra,'o','po')
            str.replace(palavra,'u','pu')
            return palavra