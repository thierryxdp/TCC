#recebe o total de passageiros e retorna quantos veículos seriam necesários para transporta-los
def carros(a,b,):
    if b==(0) or b==() and a%5!=0:
        return  a//5+1
    if b==(0) or b==() and a%5==0:
        return  a//5
    if b!=(0) or b!=() and a%b!=0:
        return a//b+1
    if b!=(0) or b!=() and a%b==0:
        return a//b
    if a==(0) and b==(0):
        return 0