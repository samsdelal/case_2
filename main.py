

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
    tax = incomes * 0.1
    print(lc.TXT_TAX1, tax, lc.TXT_TAX2)
elif (0 <= incomes <= 18150) and family == "2":
    tax = incomes * 0.1
    print(lc.TXT_TAX1, tax, lc.TXT_TAX2)
elif (0 <= incomes <= 12950) and family == "3":
    tax = incomes * 0.1
    print(lc.TXT_TAX1, tax, lc.TXT_TAX2)

elif (36901 <= incomes <= 89350) and family == "1":
    tax = incomes * 0.25
    print(lc.TXT_TAX1, tax, lc.TXT_TAX2)
elif (73801 <= incomes <= 148850) and family == "2":
    tax = incomes * 0.25
    print(lc.TXT_TAX1, tax, lc.TXT_TAX2)
elif (49401 <= incomes <= 127550) and family == "3":
    tax = incomes * 0.25
    print(lc.TXT_TAX1, tax, lc.TXT_TAX2)

elif (405101 <= incomes <= 406750) and family == "1":
    tax = incomes * 0.35
    print(lc.TXT_TAX1, tax, lc.TXT_TAX2)
elif (405101 <= incomes <= 457600) and family == "2":
    tax = incomes * 0.35
    print(lc.TXT_TAX1, tax, lc.TXT_TAX2)
elif (405101 <= incomes <= 432200) and family == "3":
    tax = incomes * 0.35
    print(lc.TXT_TAX1, tax, lc.TXT_TAX2)

# 39.6 %

elif (incomes >= 406751) and family == '1':
    tax = 0.1 * (9076 - 0) + 0.15 * (36901 - 9076) + 0.25 * (89351 - 36901) + 0.28 * (186351 - 89351) + 0.33 * (405101 - 186351) + 0.35 * (406751 - 405101) + 0.396 * (incomes - 406751)
    print("Ваш налог составит", tax, "долларов")

elif (incomes >= 457601) and family == '2':
    tax = 0.1 * (18151 - 0) + 0.15 * (73801 - 18151) + 0.25 * (148851 - 73801) + 0.28 * (226851 - 148851) + 0.33 * (405101 - 226851) + 0.35 * (457601 - 405101) + 0.396 * (incomes - 457601)
    print("Ваш налог составит", tax, "долларов")
elif (incomes >= 432201) and family == '3':
    tax = 0.1 * (12951 - 0) + 0.15 * (49401 - 12951) + 0.25 * (127551 - 49401) + 0.28 * (206601 - 127551) + 0.33 * (405101 - 206601) + 0.35 * (432201 - 405101) + 0.396 * (incomes - 432201)
