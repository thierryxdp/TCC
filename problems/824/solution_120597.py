#retorna todas as consoantes em maiúsculas
#str-->str
def uppCons(frase):
    s=''
    for caractere in frase:
        if caractere in'qwrtypsdfghjklçzxcvbnm':
            s+=caractere.upper()
        else:
            s += caractere
    return s