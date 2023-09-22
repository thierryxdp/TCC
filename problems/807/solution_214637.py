def numero_frases(texto):
    "Função na qual conta a quantidade de frases que um texto possui sendo elas separadas por ( ! , ? , . ou ...)"
    #Contagem de pontos de exclamacao
    contagem_excla = texto.count('!')
    #Contagem de pontos de interrogacao
    contagem_inter = texto.count('?')
    #Contagem de pontos finais
    contagem_final = texto.count('.')
    #Contagem de reticencias
    contagem_ret = texto.count('...')
    return contagem_excla + contagem_inter + contagem_final + contagem_ret