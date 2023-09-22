def retira_pontuacao(frase):
    if '.' in frase:
        str.replace(frase,'.','  ')
    if ',' in frase:
        str.replace(frase,',','  ')
    if '-' in frase:
        str.replace(frase,'-','  ')
    if ':' in frase:
        str.replace(frase,':','  ')
    if ';' in frase:
        str.replace(frase,';','  ')
        return str(frase)