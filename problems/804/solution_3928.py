#Start your python function here
def filtra_pares(num1, num2, num3, num4):
    tuplaP=()
    if num1%2==0:
        tuplaP += num1
        if num2%2==0:
            tuplaP += num2
            if num3%2==0:
                tuplaP += num3
                if num4%2!=0:
                    tuplaP += num4
                    return tuplap