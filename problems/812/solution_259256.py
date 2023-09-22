def retira_pontuacao(string_1:str)->str:
    def troca_valor(string_2:str)->str:
        pontuacoes = ["-",",",":",";",".","?","!"]
        return " " if string_2 in pontuacoes else string_2
    return "".join(list(map(troca_valor,string_1)))