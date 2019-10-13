

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

if (0 <= incomes <= 9075) and family == "1":
     tax = incomes*0.1
     print(lc.TXT_TAX1, tax, lc.TXT_TAX2)

elif (0 <= incomes <= 18150) and family == "2":
     tax = incomes * 0.1
     print(lc.TXT_TAX1, tax, lc.TXT_TAX2)

elif (0 <= incomes <= 12950) and family == "3":
     tax = incomes * 0.1
     print(lc.TXT_TAX1, tax, lc.TXT_TAX2)

elif (9076 <= incomes <=36900) and family == "1":
     tax = (0.1*9076)+0.15(incomes-9076)
     print(lc.TXT_TAX1, tax, lc.TXT_TAX2)

elif (18151 <= incomes <= 73800) and family == '2':
     tax = (0.1*18151)+0.15(incomes-18151)
     print(lc.TXT_TAX1, tax, lc.TXT_TAX2)

elif (12951 <= incomes <= 49400) and family = "3":
     tax = (0.1 * 12951) + 0.15(incomes - 12951)
     print(lc.TXT_TAX1, tax, lc.TXT_TAX2)

elif (186351 <= incomes <= 405100) and family = "1":
     tax = (0.1*9076)+0.15(36901-9076)+0.25(89351-36901)+0.28(186351-89351)+0.33(incomes-186351)
     print(lc.TXT_TAX1, tax, lc.TXT_TAX2)

elif (186351 <= incomes <= 405100) and family = "2":
     tax = (0.1*18151)+0.15(73801-18151)+0.25(148851-73801)+0.28(226851-148851)+0.33(incomes-226851)
     print(lc.TXT_TAX1, tax, lc.TXT_TAX2)

elif (186351 <= incomes <= 405100) and family = "3":
     tax = (0.1*12951)+0.15(49401-12951)+0.25(127551-49401)+0.28(206601-127551)+0.33(incomes-206601)
     print(lc.TXT_TAX1, tax, lc.TXT_TAX2)






