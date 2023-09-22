def inverte(frase):
    frase=frase.lower()
    frase1=frase.split('.')
    frase2=' '.join(frase1)
    frase3=frase2.split(',')
    frase4=' '.join(frase3)
    frase5=frase4.split(';')
    frase6=' '.join(frase5)
    frase7=frase6.split(':')
    frase8=' '.join(frase7)
    frase9=frase8.split('?')
    frase10=' '.join(frase9)
    frase11=frase10.split('!')
    frase12=frase[::-1]
    frase13=' '.join(frase12)
    return frase13