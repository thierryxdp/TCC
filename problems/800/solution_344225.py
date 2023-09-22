def total(toBuyList, productsAndPrices):
    '''Function that, given a to buy list and a dictionary 
    with the products of a marketplace and it`s prices, returns
    the total value of the purchase.
    List, Dict --> Float'''
    totalValue = 0
    for i in toBuyList:
        if i in productsAndPrices:
            productValue = dict.get(productsAndPrices, i)
            totalValue = totalValue + productValue
    return round(totalValue,2)