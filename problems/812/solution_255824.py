def retira_pontuacao(frase):
   '''Substitui toda a pontuação (vírgula,travessão,
      dois pontos, ponto com vírgula e ponto final)
      da frase por espaço;str->str'''
   if '.' in frase:
    return str.replace(frase,'.',' ')
   if ',' in frase:
       return str.replace(frase,',',' ')
   if '-' in frase:
       return str.replace(frase,'-',' ')
   if ';' in frase:
       return str.replace(frase,';',' ')
   if ':' in frase:
       return str.replace(frase,':',' ')