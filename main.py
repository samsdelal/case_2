

# string constants
"""Case-study #0 My first code
Developers:
Makarov A (39.999999%), Kuznecov B(30%), Odoevcev S(50%)


"""
"""name_month = [JAN, FAB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC]

annual_income = 0
for month in range(12):
    print('{} {}:'.format(QUESTION,name_month[month], end ='')
    income = float(input())
    annual_income += income
print(annual_income)"""

import local as lc

family = input(lc.TXT_STATUSFAM0 + "\n" +
               "\n" +
               lc.TXT_STATUSFAM1 + "\n" +
               lc.TXT_STATUSFAM2 + "\n" +
               lc.TXT_STATUSFAM3 + "\n" +
               "---")
print('---------------------------')
incomes = int(input(lc.TXT_INPCOM + "--- "))

if (0 < incomes < 9075) and family == "1":
    tax = incomes*0.1
    print(lc.TXT_TAX1, tax, lc.TXT_TAX2)
elif (0 < incomes < 18150) and family == "2":
    tax = incomes * 0.1
    print(lc.TXT_TAX1, tax, lc.TXT_TAX2)
elif (0 < incomes < 12950) and family == "3":
    tax = incomes * 0.1
    print(lc.TXT_TAX1, tax, lc.TXT_TAX2)





