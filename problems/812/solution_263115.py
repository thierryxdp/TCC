def retira_pontuacao(frase):
    ''' função que dada uma frase retira as pontuações existentes,e as substitui
por ' '(str de espaço).
str->str'''
   s=frase
   trave=str.replace(s,'-',' ')
   vir=str.replace(trave,',',' ')
   dp=str.replace(vir,':',' ')
   pv=str.replace(dp,';',' ')
   inte=str.replace(pv,'?',' ')
   exc=str.replace(inte,'!',' ')
   ret=str.replace(exc,'...',' ')
   pf=str.replace(ret,'.',' ')
   return pf