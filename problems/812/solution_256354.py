def retira_pontuacao(frase):
   '''Substitui toda a pontuação (vírgula,travessão,
      dois pontos, ponto com vírgula e ponto final)
      da frase por espaço;str->str'''
   ponto=str.replace(frase,'.',' ')
   exclamacao=str.replace(ponto,'!',' ')
   travessao=str.replace(exclamacao,'-',' ')
   interrogacao=str.replace(travessao,'?',' ')
   pvirgula=str.replace(interrogacao,';',' ')
   doispontos=str.replace(pvirgula,':',' ')
   virgula=str.replace(doispontos,',',' ')
   string=virgula
   return string