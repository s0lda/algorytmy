income = int(input('What\'s you income?:''\n')
# Tax Free Allowance
tax_free = 12500
taxpayable = 0
# Tax Bands
sAmount = 50000
hAmount = 100000
aAmount = 150000
# in UK over 100k income will reduce tax free allowance. every £2 will reduce allowance by £1
all_red = (income - hAmount) / 2
# over 100k you start loosing allowance, that's the end of it.
allStop = tax_free * 2

print('Income ', income)

if income <= 12500:
    taxpayable = 0
elif income <= sAmount:
    taxpayable = (income - tax_free) * 20 / 100
elif income <= aAmount:
    if income > sAmount and income <= hAmount:
        taxpayable = ((sAmount - tax_free) * 20 / 100) + ((income - sAmount) * 40 / 100)
    elif income > hAmount and income <= (hAmount + allStop):
        # lower band(including tax allowance) @ 20% + income - higher band @ 40% + allowance reduction @ 40%
        taxpayable = ((sAmount - tax_free) * 20 / 100) + ((hAmount - sAmount) * 40 / 100 ) + ((income - hAmount + all_red) * 40 / 100)
    elif income > (hAmount + allStop) and income <= aAmount:
        # higher band + tax allowance * 2 = no Tax free allowance anymore 
        taxpayable = ((sAmount - tax_free) * 20 / 100) + ((income - sAmount) * 40 / 100) + (tax_free * 40 / 100)
elif income > aAmount:
    taxpayable = 52500 + ((income - 150000) * 45 / 100)

print('Total tax to pay is: ', taxpayable)
