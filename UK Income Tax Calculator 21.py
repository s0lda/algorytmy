income = int(input('Enter your salary: ''\n'))
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

#NI contribution
weeklywage = income / 52
ni1 = 183
ni2 = 962

# calculating the amount of tax owed

# tax free amount
if income <= 12500:
    taxpayable = 0
# 20% rate
elif income <= sAmount:
    taxpayable = (income - tax_free) * 20 / 100
# 40% rate
elif income <= aAmount:
    # 40% rate for below 100k income
    if income > sAmount and income <= hAmount:
        taxpayable = ((sAmount - tax_free) * 20 / 100) + ((income - sAmount) * 40 / 100)
    # 40% rate for over 100k with reducing tax allowance
    elif income > hAmount and income <= (hAmount + allStop):
        # lower band(including tax allowance) @ 20% + income - higher band @ 40% + allowance reduction @ 40%
        taxpayable = ((sAmount - tax_free) * 20 / 100) + ((hAmount - sAmount) * 40 / 100 ) + ((income - hAmount + all_red) * 40 / 100)
    # 40% rate for over 100k with no tax allowance left
    elif income > (hAmount + allStop) and income <= aAmount:
        # higher band + tax allowance * 2 = no Tax free allowance anymore 
        taxpayable = ((sAmount - tax_free) * 20 / 100) + ((income - sAmount) * 40 / 100) + (tax_free * 40 / 100)
# calculating 45% rate
elif income > aAmount:
    taxpayable = 52500 + ((income - 150000) * 45 / 100)

# calculating National Insurance contribution

# NI rate free amount
if weeklywage <= ni1:
    ni = 0
# calculating 12 % NI rate
elif weeklywage > ni1 and weeklywage <= ni2:
    ni = ((weeklywage - ni1) * 12 / 100) * 52
# calculating 2% NI rate
elif weeklywage > ni2:
    ni = ((((weeklywage - ni1) - abs(ni2 - weeklywage)) * 12 / 100) + ((weeklywage - ni2) * 2 / 100)) * 52

# total deductions and home take
totalded = taxpayable + ni
home = income - totalded

print('Total tax to pay is: ', taxpayable)
print('You NI contribution is: ', round(ni, 2))
print('Total deductions: ', totalded)
print('Your home take is: ', round(home, 2))