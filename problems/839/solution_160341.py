#recebe o total de passageiros e retorna quantos veículos seriam necesários para transporta-los
def carros(a,b,):
    if b==() and a%5!=int:
        return  a//5+1
    if b==() and a%5==int:
        return  a//5
    if b!=() and a%b!=int:
        return a//b+1
    if b!=() and a%b==int:
        return a//b
    if a==(0):
        return 0