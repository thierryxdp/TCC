'''função que dado uma frase qualquer, ela inverte a ordem da frase e retira as sua pontuação
str->str'''

def inverte(frase):
    mudanca1=str.replace(frase,'-',' ')
    mudanca2=str.replace(mudanca1,':',' ')
    mudanca3=str.replace(mudanca2,';',' ')
    mudanca4=str.replace(mudanca3,'!',' ')
    mudanca5=str.replace(mudanca4,'?',' ')
    mudanca6=str.replace(mudanca5,',',' ')
    mudanca7=str.replace(mudanca6,'.',' ')
    letra_minuscula=str.lower(mudanca7)
    lista_palavra=str.split(letra_minuscula)
    lista_inversa=lista_palavra[::-1]
    
    return str.join(' ',lista_inversa)