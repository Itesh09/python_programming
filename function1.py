# first program for printing the price of phone after discount price and original price is 40000
price=40000
discount=int(input("enter theamount of discount"))

def price_after_discount(discount):
    print(price-discount*price/100)
    return price-discount*price


price_after_discount(discount)
    
