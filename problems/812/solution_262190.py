def retira_pontuacao (texto):
    
     subs1 = str.replace(texto,'-',' ')
     subs2 = str.replace(subs1,',',' ')
     subs3 = str.replace(subs2,'!',' ')
     subs4 = str.replace(subs3,'.',' ')
     subs5 = str.replace(subs4,'?',' ')
     subs6 = str.replace(subs5,':',' ')
     subs7 = str.replace(subs6,';',' ')

     return subs7