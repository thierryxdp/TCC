def uppCons(phrase):
    answer = ""
    for letter in phrase:
        if letter not in "aeiouAEIOU":
            answer = answer + letter.upper()
    return answer