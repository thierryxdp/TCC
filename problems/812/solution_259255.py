def retira_pontuacao(string_1:str)->str:
    def troca_valor(string_2:str)->str:
        pontuacoes = ["-",",",":",";",".","?","!"]
        return " " if string_2 in pontuacoes else string_2
    str_aux = ""
    for c in map(troca_valor,string_1):
        str_aux+=c
    return str_aux