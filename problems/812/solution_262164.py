def retira_pontuacao(frase):
    
    novo1 = frase.split("-")
    novo2 = frase.split(",")
    novo3 = frase.split(":")
    novo4 = frase.split(";")
    novo5 = frase.split(".")
    novo6 = frase.split("?")
    novo7 = frase.split("!")
    novo8 = frase.split("...")
    
    return (novo1 + novo2 + novo3 + novo4 + novo5 + novo6 + novo7 + novo8)