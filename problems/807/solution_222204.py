def conta_frases(frase):
    """conta o número de frases no texto"""
    ocorrencia = 0
    pontos =  str.count(frase,'.')
    exclama= str.count(frase,'!')
    interroga = str.count(frase,'?')
    trespt = str.count(str.replace(frase,'...','***',100))
    ocorrencia = pontos+exclama+interroga+trespt
    
    return ocorrencia