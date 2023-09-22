def retira_pontuacao(frase):
    """
    funcao retira toda a pontuacao em frase dada como entrada
    str---->str
    """
   frase = str.replace(frase,'-',' ')
   frase = str.replace(frase,',',' ')
   frase = str.replace(frase,':',' ')
   frase = str.replace(frase,';',' ')
   frase = str.replace(frase,'.',' ')
   frase = str.replace(frase,'!',' ')
   frase = str.replace(frase,'?',' ')
   return frase