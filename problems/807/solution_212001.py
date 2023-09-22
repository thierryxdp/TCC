"""Recebe uma string e retorna a quantidade de frases nela, baseada 
nas pontuações"""
"""str->int"""
	def conta_frases(texto):
        pt_fianl = texto.count(".")
        reticencias = texto.count("...")
        exclamacao = texto.count("!")
        interrogacao = texto.count("?")
        return pt_final + reticencias + exclamacao + interrogacao