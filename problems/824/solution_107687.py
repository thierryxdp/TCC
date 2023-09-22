def uppCons(frase):
 answer = ""
    for letter in frase:
        if letter not in "aeiouáéíóúâãõà":
            answer = answer + letter.upper()
        else:
            answer = answer + letter
    return answer


print(uppCons(input("Enter a phrase: ")))