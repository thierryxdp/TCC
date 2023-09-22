def colchao(medidas,h,l):
    passa=true
    naopassa=false
    if   medidas[1]<h:
         passa
    if  medidas[0]<l:
         passa
    if   medidas[1]>h:
         naopassa
   
    passa=true
    naopassa=false
    return passa or naopassa