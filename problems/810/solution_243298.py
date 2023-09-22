def inverte(frase):
    separa = frase.split(' ')
    separa = separa[::-1]
    return ((',' .join(separa)).replace(',',' '))