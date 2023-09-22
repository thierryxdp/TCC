def uppCons(f):
    """"Função que retorna as cosoantes das frases em letra maiúsculas
        str->str"""
    proximo=0
    stringnova=''
    while proximo < len(f):
        proximo=proximo+1
        if f(proximo) not in 'AEIOUaeiou':
            str.upper(proximo)
            stringnova= stringnova + f[proximo]
    return stringnova