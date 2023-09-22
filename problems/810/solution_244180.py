def inverte(frase):
    """função recebe frase e usa a função replace pra inverter"""
    frase = frase.replace('!','')
    frase = frase.replace('?','')
    frase = frase.replace(',','')
    frase = frase.replace('.','')
    frase = frase.replace('-',' ')
    invertida = (str.split(frase,' '))
    lista = (str.join(' ',invertida[::-1]))
    return lista.lower()