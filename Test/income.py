# 收入计算器（北京2018）

# 养老保险
rate_old_private = 0.08
rate_old_enterprise = 0.19
# 医疗保险
rate_medical_private = 0.02
rate_medical_enterprise = 0.1
# 失业保险
rate_unemployed_private = 0.002
rate_unemployed_enterprise = 0.01
# 工伤保险
rate_accident_private = 0.0
rate_accident_enterprise = 0.005
# 生育保险
rate_born_private = 0.0
rate_born_enterprise = 0.008

# 住房公积金
rate_home_private = 0.12
rate_home_enterprise = 0.12

# 社保&公积金 缴纳基数上线 25401
base_money_limit = 25401
# 个税起征金额
base_tax = 3500

def main():
    income = int(input("income:").title())
    money = float_fun_final_income(income)

def float_fun_final_income(income):
    if income > base_money_limit:
        base_money = base_money_limit
    else:
        base_money = income
    # base_money = 12000

    old_private = base_money * rate_old_private
    old_enterprise = base_money * rate_old_enterprise
    medical_private = base_money * rate_medical_private
    medical_enterprise = base_money * rate_medical_enterprise
    unemployed_private = base_money * rate_unemployed_private
    unemployed_enterprise = base_money * rate_unemployed_enterprise
    accident_private = base_money * rate_accident_private
    accident_enterprise = base_money * rate_accident_enterprise
    born_private = base_money * rate_born_private
    born_enterprise = base_money * rate_born_enterprise
    home_private = base_money * rate_home_private
    home_enterprise = base_money * rate_home_enterprise

    insurance_private = old_private + medical_private + unemployed_private + accident_private + born_private + home_private
    insurance_enterprise = old_enterprise + medical_enterprise + unemployed_enterprise + accident_enterprise + born_enterprise + home_enterprise

    print("个人缴纳保险公积金:", insurance_private, "其中公积金:", home_private)
    print("企业缴纳保险公积金:", insurance_enterprise, "其中公积金:", home_enterprise)

    # 扣除保险公积金后的金额（需要缴纳个税）
    income_insurace = income - insurance_private
    tax = float_fun_tax(income_insurace)
    print("缴纳个税:", tax)
    money = income_insurace - tax
    print("收入:", money)
    print("总价值:", money + insurance_private + insurance_enterprise)

    return money

def float_fun_tax(income):
    tax_income = income - base_tax
    tax_rate = 0.0
    base_tax_money = 0

    if tax_income <= 1500:
        tax_rate = 0.03
        base_tax_money = 0
    elif 1500 < tax_income <= 4500:
        tax_rate = 0.1
        base_tax_money = 105
    elif 4500 < tax_income <= 9000:
        tax_rate = 0.2
        base_tax_money = 555
    elif 9000 < tax_income <= 35000:
        tax_rate = 0.25
        base_tax_money = 1005
    elif 35000 < tax_income <= 55000:
        tax_rate = 0.3
        base_tax_money = 2755
    elif 55000 < tax_income <= 80000:
        tax_rate = 0.35
        base_tax_money = 5505
    elif 80000 < tax_income:
        tax_rate = 0.45
        base_tax_money = 13505

    tax =  tax_income * tax_rate - base_tax_money
    return tax


main()
