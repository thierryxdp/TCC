def uppCons(frase):
     answer = ""
    for letter in phrase:
        if letter in "qwrtypsdfghjklzxcvbnmç":
            answer = answer + letter.upper()
        else:
            answer = answer + letter
    return answer


print(uppCons(input("Enter a frase: ")))