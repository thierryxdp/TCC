def retira_pontuacao(frase):
    frase_nova = []
    if '.' in frase:
        frase_nova = frase_nova + str.replace(frase,'.',' ')
    if ',' in frase:
        frase_nova = frase_nova + str.replace(frase,',',' ')
    if '-' in frase:
        frase_nova = frase_nova + str.replace(frase,'-',' ')
    if ':' in frase:
        frase_nova = frase_nova + str.replace(frase,':',' ')
    if ';' in frase:
        frase_nova = frase_nova + str.replace(frase,';',' ')
        return frase_nova