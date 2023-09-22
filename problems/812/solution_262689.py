def retira_pontuacao(frase):

palavra=str.replace(frase,'?',' ')
palavra = str.replace(palavra'.',' ')
palavra= str.replace(palavra,',',' ')
palavra= str.replace(palavra,'!',' ')
palavra= str.replace(palavra,'-',' ')
return palavra