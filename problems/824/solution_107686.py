def uppCons(frase):
 answer = ""
    for letter in phrase:
        if letter not in "aeiouáéíóúâãõà":
            answer = answer + letter.upper()
        else:
            answer = answer + letter
    return answer


print(uppCons(input("Enter a phrase: ")))