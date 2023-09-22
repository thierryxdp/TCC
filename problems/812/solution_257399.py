def retira_pontuacao(frase):
    batata = str.replace(frase, ".",' ')
    batata = str.replace(batata, "!",' ')
    batata = str.replace(batata, "?",' ')
    batata = str.replace(batata, ",",' ')
    batata = str.replace(batata, "-",' ')
    batata = str.replace(batata, ":",' ')
    batata = str.replace(batata, ";",' ')
    batata = str.replace(batata, "...",' ')
    batata = str.replace(batata, "_",' ')
    return batata