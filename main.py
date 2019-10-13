import local as lc

# string constants
"""Case-study #2 - USA TAX CALCULATOR
Developers:
Makarov A (40%), Kuznecov B(40%), Odoevcev S(40%)"""


family = input(lc.TXT_STATUSFAM0 + "\n" +
               "\n" +
               lc.TXT_STATUSFAM1 + "\n" +
               lc.TXT_STATUSFAM2 + "\n" +
               lc.TXT_STATUSFAM3 + "\n" +
               "--- ")
print('---------------------------')
name_month = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
QUESTION = 'Какой доход за месяц?'
annual_income = 0
for month in range(12):
 print('{} {}:'.format(QUESTION,name_month[month], end =''))
 income = float(input())
 annual_income += income
 incomes = annual_income
print('Ваш годовой доход составил - ', incomes,lc.TXT_TAX2)
print('---------------------------')
#10
if (0 <= incomes <= 9075) and family == "1":
    tax = incomes * 0.1
    print(lc.TXT_TAX1, tax, lc.TXT_TAX2)
elif (0 <= incomes <= 18150) and family == "2":
    tax = incomes * 0.1
    print(lc.TXT_TAX1, tax, lc.TXT_TAX2)
elif (0 <= incomes <= 12950) and family == "3":
    tax = incomes * 0.1
    print(lc.TXT_TAX1, tax, lc.TXT_TAX2)

#15
elif (9076 <= incomes <=36900) and family == "1":
     tax = (0.1*9076)+0.15*(incomes-9076)
     print(lc.TXT_TAX1, tax, lc.TXT_TAX2)

elif (18151 <= incomes <= 73800) and family == '2':
     tax = (0.1*18151)+0.15*(incomes-18151)
     print(lc.TXT_TAX1, tax, lc.TXT_TAX2)

elif (12951 <= incomes <= 49400) and family == "3":
     tax = (0.1 * 12951) + 0.15*(incomes - 12951)
     print(lc.TXT_TAX1, tax, lc.TXT_TAX2)
    
# 25%
elif (36901 <=  incomes <= 89350) and family == '1':
    tax = 0.1 * (9076 - 0) + 0.15 * (36901 - 9076) + 0.25 * (incomes - 36901)
    print(lc.TXT_TAX1, tax, lc.TXT_TAX2)

elif (73801 <= incomes <= 148850) and family == '2':
    tax = 0.1 * (18151 - 0) + 0.15 * (73801 - 18151) + 0.25 * (incomes - 73801)
    print(lc.TXT_TAX1, tax, lc.TXT_TAX2)

elif (49401 <= incomes <= 127550 ) and family == '3':
    tax = 0.1 * (12951 - 0) + 0.15 * (494011 - 12951) + 0.25 * (incomes - 49401)
    print(lc.TXT_TAX1, tax, lc.TXT_TAX2)
    
# 28%

elif (89351 <=  incomes <= 186350) and family == '1':
    tax = 0.1 * (9076 - 0) + 0.15 * (36901 - 9076) + 0.25 * (89351 - 36901) + 0.28 * (incomes - 89351)
    print(lc.TXT_TAX1, tax, lc.TXT_TAX2)

elif (148851 <= incomes <= 226850) and family == '2':
    tax = 0.1 * (18151 - 0) + 0.15 * (73801 - 18151) + 0.25 * (148851 - 73801) + 0.28 * (incomes - 148851)
    print(lc.TXT_TAX1, tax, lc.TXT_TAX2)

elif (127551 <= incomes <= 206600 ) and family == '3':
    tax = 0.1 * (12951 - 0) + 0.15 * (494011 - 12951) + 0.25 * (127551 - 49401) + 0.28 * (incomes - 127551)
    print(lc.TXT_TAX1, tax, lc.TXT_TAX2)

#33    
elif (186351 <= incomes <= 405100) and family == "1":
     tax = (0.1*9076)+0.15*(36901-9076)+0.25*(89351-36901)+0.28*(186351-89351)+0.33*(incomes-186351)
     print(lc.TXT_TAX1, tax, lc.TXT_TAX2)

elif (186351 <= incomes <= 405100) and family == "2":
     tax = (0.1*18151)+0.15*(73801-18151)+0.25*(148851-73801)+0.28*(226851-148851)+0.33*(incomes-226851)
     print(lc.TXT_TAX1, tax, lc.TXT_TAX2)

elif (186351 <= incomes <= 405100) and family == "3":
     tax = (0.1*12951)+0.15*(49401-12951)+0.25*(127551-49401)+0.28*(206601-127551)+0.33*(incomes-206601)
     print(lc.TXT_TAX1, tax, lc.TXT_TAX2)


# 35%
elif (405101 <= incomes <= 406750) and family == '1':
    tax = 0.1 * (9076 - 0) + 0.15 * (36901 - 9076) + 0.25 * (89351 - 36901) + 0.28 * (186351 - 89351) + 0.33 * (405101 - 186351) + 0.35 * (incomes - 405101)
    print(lc.TXT_TAX1, tax, lc.TXT_TAX2)
elif (405101 <= incomes >= 457600) and family == '2':
    tax = 0.1 * (18151 - 0) + 0.15 * (73801 - 18151) + 0.25 * (148851 - 73801) + 0.28 * (226851 - 148851) + 0.33 * (405101 - 226851) + 0.35 * (incomes - 405101)
    print(lc.TXT_TAX1, tax, lc.TXT_TAX2)
elif (405101 <= incomes <= 432200 ) and family == '3':
    tax = 0.1 * (12951 - 0) + 0.15 * (49401 - 12951) + 0.25 * (127551 - 49401) + 0.28 * (206601 - 127551) + 0.33 * (405101 - 206601) + 0.35 * (incomes - 405101)
    print(lc.TXT_TAX1, tax, lc.TXT_TAX2)


# 39.6 %

elif (incomes >= 406751) and family == '1':
    tax = 0.1 * (9076 - 0) + 0.15 * (36901 - 9076) + 0.25 * (89351 - 36901) + 0.28 * (186351 - 89351) + 0.33 * (405101 - 186351) + 0.35 * (406751 - 405101) + 0.396 * (incomes - 406751)
    print(lc.TXT_TAX1, tax, lc.TXT_TAX2)
elif (incomes >= 457601) and family == '2':
    tax = 0.1 * (18151 - 0) + 0.15 * (73801 - 18151) + 0.25 * (148851 - 73801) + 0.28 * (226851 - 148851) + 0.33 * (405101 - 226851) + 0.35 * (457601 - 405101) + 0.396 * (incomes - 457601)
    print(lc.TXT_TAX1, tax, lc.TXT_TAX2)
elif (incomes >= 432201) and family == '3':
    tax = 0.1 * (12951 - 0) + 0.15 * (49401 - 12951) + 0.25 * (127551 - 49401) + 0.28 * (206601 - 127551) + 0.33 * (405101 - 206601) + 0.35 * (432201 - 405101) + 0.396 * (incomes - 432201)
    print(lc.TXT_TAX1, tax, lc.TXT_TAX2)
