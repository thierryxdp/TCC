def conta_frases (texto: str) -> int:
    '''Recebe um texto e retorna a quantidade de frases.
    Frases são delimitadas por:
    	"?", "!", ".", "..."
    '''
    conta_ponto_final = str.count(texto, ".")
    conta_exclamacao = str.count(texto, "!")
    conta_interrogacao = str.count(texto, "?")
    conta_reticencias = str.count(texto, "...")
    #Retira de conta_ponto_final as vezes que contou ponto final como reticencias
    conta_ponto_final -= 3*conta_reticencias
    quantas_frases = conta_ponto_final + conta_exclamacao + conta_interrogacao + conta_reticencias
    return quantas_frases