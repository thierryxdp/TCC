def conta_frases(frase):
    """conta o número de frases no texto"""
    ocorrencia = 0
    trespt = str.count(str.replace(frase,'...','***',100),'***')
    pontos =  str.count(frase,'.')
    exclama= str.count(frase,'!')
    interroga = str.count(frase,'?')
    ocorrencia = pontos+exclama+interroga+trespt
    
    return ocorrencia