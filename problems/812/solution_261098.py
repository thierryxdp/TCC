def retira_pontuacao(frase):
    if str(.) in frase:
        str.replace(frase,'.','  ')
    if str(,) in frase:
        str.replace(frase,',',  )
    if str(-) in frase:
        str.replace(frase,'-',  )
    if str(:) in frase:
        str.replace(frase,':',  )
    if str(;) in frase:
        str.replace(frase,';','  ')
        return str(frase)