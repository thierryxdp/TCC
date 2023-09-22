def uppCons(string_1:str)->str:
    vogais = 'aeiouãáâàéêíîõóôúû'
    vogais += vogais.upper()
    def troca_letra(string_2:str)->str:
        return string_2 if string_2 in vogais else string_2.upper()
    return "".join(map(troca_letra,string_1))