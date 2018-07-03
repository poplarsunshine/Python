
def one_year_money(years, rate, money):
    return money * (1 + rate) ** years

def every_year_money(years, rate, a_money):
    money = 0
    for index in range(years):
        bx = one_year_money((index + 1), rate, a_money)
        money += bx
    return money

current_age = 33    # 现在的年龄
rate = 0.0275   # 年利率
every_year_save_money = 40800 # 每年存入金额
save_years = 20  # 持续存入年数

age = int(input("age:" ).title())

if age > current_age:
    keep_year = age - current_age
    bx = 0
    if keep_year > save_years:
        in_bx = every_year_money(save_years, rate, every_year_save_money)
        bx = one_year_money(keep_year - save_years, rate, in_bx)
    else:
        save_years = keep_year
        bx = every_year_money(save_years, rate, every_year_save_money)
    print("\n{}岁\n价值:{}\n".format(age, int(bx)))
else:
    print("\n请输入大于{}的年龄".format(current_age))
