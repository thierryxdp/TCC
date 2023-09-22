#recebe o total de passageiros e retorna quantos veículos seriam necesários para transporta-los
def carros(a,b,c):
    c=a//b
    if b==(0):
        c=a//5
    if a%b or a%5!=0:
        c=c+1
    return c