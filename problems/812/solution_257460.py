def retira_pontuacao(frase):
    pontuações = ["..." , ".", "!" , "?" , ";" , ":" , "-" , ","]
    frasen=frase
    frasen= frasen.replace("..." , " ")
    frasen= frasen.replace(":" , " ")
    frasen= frasen.replace("!" , " ")
    frasen= frasen.replace("?" , " ")
    frasen= frasen.replace(";" , " ")
    frasen= frasen.replace("." , " ")
    frasen= frasen.replace("-" , " ")
    frasen= frasen.replace("," , " ")
    return frasen