def retira_pontuacao(texto):
   x=str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(texto,':','#'),';','#'),',','#'),'-','#'),'.','#'),'!','#'),'?','#')
   return str.replace('#',' ')