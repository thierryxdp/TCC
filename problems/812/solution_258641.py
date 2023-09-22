'''função que dado uma frase qualquer, subistitui toda a pontuação dessa frase por espaço
str->str'''
def retira_pontuacao(frase):
    mudanca1=str.replace(frase,'-',' ')
    mudanca2=str.replace(mudanca1,':',' ')
    mudanca3=str.replace(mudanca2,';',' ')
    mudanca4=str.replace(mudanca3,'!',' ')
    mudanca5=str.replace(mudanca4,'?',' ')
    mudanca6=str.replace(mudanca5,',',' ')
    mudanca7=str.replace(mudanca6,'.',' ')
    
    return mudanca7