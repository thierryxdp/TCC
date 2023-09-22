def retira_pontuacao(string):
    """Retorna uma frase onde todos os caracteres de pontuação foram substituídos por espaço; string -> string."""
    string = str.replace(string,"!"," ")
    string = str.replace(string,"?"," ")
    string = str.replace(string,"..."," ")
    string = str.replace(string,"."," ")
    string = str.replace(string,","," ")
    string = str.replace(string,"-"," ")
    string = str.replace(string,";"," ")
    return string