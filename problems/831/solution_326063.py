def lingua_p(palavra):
    """Função que recebe uma palavra e retorna a mesma palavra só que com a lingua p; str ->str""" 
    i = 0
    traducao = ''
    vogal = 'AEIOUÁÉÍÓÚÂÊÎÔÃÕÀaeiouáéíóúâêîôãõà'
    while i < len(palavra):
        if palavra[i]in vogal:
            traducao = traducao + palavra[i] + 'p' + palavra[i]
        else:
            traducao = traducao + palavra[i]
        i = i + 1
    return str.lower(traducao)