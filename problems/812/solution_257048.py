def retira_pontuacao(frase):
    """substitui pontuações ortograficas por espaços--> Str,Str"""
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