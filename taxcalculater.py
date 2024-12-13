def taxcalc(bill,taxamount):
    '''caculate and pay the total amount you will need to pay at the shop/resteront'''
    tax=(bill*taxamount)/100
    total= bill+tax
    print("the amout of the bill alone",bill)
    print("tax percentage",taxamount)
    print("ow much tax was added on the payment",tax)
    print("the total amount you need to pay",total)
taxcalc(2500,10)