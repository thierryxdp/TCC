# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def retira_pontuacao(frase):
" essa funcao calcula e retorna uma frase onde todos os carateres tenham sido substituido por espaco; str -> str"
   filtro1=str.replace(frase,'-',' ')
   filtro2=str.replace(filtro1,':',' ')
   filtro3=str.replace(filtro2,';',' ')
   filtro4=str.replace(filtro3,'!',' ')
   filtro5=str.replace(filtro4,'?',' ')
   filtro6=str.replace(filtro5,',',' ')
   filtro7=str.replace(filtro6,'.',' ')

   return filtro7