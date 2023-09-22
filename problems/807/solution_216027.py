def conta_frases(t):
    	"""Função que dado um texto(t) retorna o número de frases presentes nele. string --> int"""
        return str.partition(t, ".") + str.partition(t, "!") + str.partition(t, "?") + str.partition(t, "...")