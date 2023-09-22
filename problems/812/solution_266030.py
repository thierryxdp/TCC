def retira_pontuacao(frase):
    sim_pon=["'", '"', ",", ".", "!", ":", ";", '#', '@']
    texto=frase.replace("sim_pon", " ")
    return texto