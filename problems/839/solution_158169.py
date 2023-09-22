def carros (pessoas, vagas=5):
'''Definir quantos carros serão necessário de acordo com  a quantidade de passageiros'''
    if pessoas <=0 :
        return (0)
    if pessoas >=1 and pessoas <= 5 :
        return round(pessoas// vagas)
    if pessoas >=6 and pessoas <= 10 :
        return round(pessoas// vagas + 1 )
    if pessoas >=11 and pessoas <= 15 :
        return round(pessoas// vagas + 2 )
    if pessoas >=16 and pessoas <= 20 :
        return round(pessoas// vagas + 3 )