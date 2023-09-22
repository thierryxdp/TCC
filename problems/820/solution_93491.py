#A palavra, a letra e a ocorrencia serao dadas pelo usuario
string = input("Escreva uma palavra: ")
letra = input("Diga qual letra da palavra escolhida: ")
ocorrencia = input(input("Qual ocorrencia dela quer encontrar?: "))

def posLetra(x,y,z):
    """funcao que recebe uma palavra(x), uma letra(y) e um numero(z) e indica a ocorrencia
    desejada da letra, str,str,int->int"""
    achar = x.find(y)
    while achar >= 0 and z > 1:
        achar = x.find(y, achar+1)
        z -= 1
        return achar
print(posLetra(string, letra, ocorrencia))