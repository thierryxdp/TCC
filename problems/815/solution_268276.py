def altera_frase(dados):
    """Função que recebe uma palavra, uma frase e uma posição e faz ajustes 
    conforme detalhado no enunciado da questão."""
    """list-->str"""
    if dados[1] in dados[0]:
        return str.replace(dados[0],dados[1],str.upper(dados[1]),1)
    else:
        resultado=list.insert(str.split("dados[0]"),dados[2],dados[1])
        return resultado