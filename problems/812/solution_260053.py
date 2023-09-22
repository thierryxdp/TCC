def retira_pontuacao(texto):
    if "-" or "," or ":" or ";" or "." in texto:
        a="-"
        b=","
        c=":"
        d=";"
        e="."
        
        a=" "
        return texto