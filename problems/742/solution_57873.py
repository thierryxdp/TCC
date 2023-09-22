def substitui(s,x,i):
    """função que troca de posição as variaveis 'x' e 'i'
ex: substitui('leo',2,1)  - ('leo',1,2)
o numero int 'i' deve ser >= 0 e <=comprimento da str
str,int,int -> str""" #diversos tipos, pois a finção consegue suportar
    if i >= 0 and i <= len(s): 
        return (str(s),i,x)
    else: #utilizando else caso o numero do comp da str ñ coincida, logo volta nada
        return