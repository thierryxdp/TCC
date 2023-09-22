#recebe o total de passageiros e retorna quantos veículos seriam necesários para transporta-los
def carros(a,b,):
    if b==(0) and a%5!=0:
        return  a//5+1
    if b==(0) and a%5==0:
        return  a//5
    if b!=(0) and a%b!=0:
        return a//b+1
    if b!=(0) and a%b==0:
        return a//b