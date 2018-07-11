# 收入计算器（北京2018）
import argparse

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
    income = int(input("税前工资:").title())
    money = float_fun_final_income(income)

def float_fun_final_income(income):
    in_arg = get_input_args()
    base_limit = in_arg.base_limit

    if income > base_limit:
        base_money = base_limit
    else:
        base_money = income

    old_private = int(base_money * rate_old_private)
    old_enterprise = int(base_money * rate_old_enterprise)
    medical_private = int(base_money * rate_medical_private)
    medical_enterprise = int(base_money * rate_medical_enterprise)
    unemployed_private = int(base_money * rate_unemployed_private)
    unemployed_enterprise = int(base_money * rate_unemployed_enterprise)
    accident_private = int(base_money * rate_accident_private)
    accident_enterprise = int(base_money * rate_accident_enterprise)
    born_private = int(base_money * rate_born_private)
    born_enterprise = int(base_money * rate_born_enterprise)
    home_private = int(base_money * rate_home_private)
    home_enterprise = int(base_money * rate_home_enterprise)

    insurance_private = old_private + medical_private + unemployed_private + accident_private + born_private + home_private
    insurance_enterprise = old_enterprise + medical_enterprise + unemployed_enterprise + accident_enterprise + born_enterprise + home_enterprise

    print("%-10s %-8s %-10s" % ("项目名称", "个人", "企业"))
    print("%-10s %-10s %-10s" % ("养老保险", old_private, old_enterprise))
    print("%-10s %-10s %-10s" % ("医疗保险", medical_private, medical_enterprise))
    print("%-10s %-10s %-10s" % ("工伤保险", accident_private, accident_enterprise))
    print("%-10s %-10s %-10s" % ("生育保险", born_private, born_enterprise))
    print("%-10s %-10s %-10s" % ("住房积金", home_private, home_enterprise))
    print("---")
    print("%-9s -%-10s -%-10s =-%d" % ("总计缴纳", insurance_private, insurance_enterprise, insurance_private + insurance_enterprise))

    # 扣除保险公积金后的金额（需要缴纳个税）
    income_insurace = income - insurance_private
    tax = float_fun_tax(income_insurace)
    print("%-9s -%-10s" % ("缴纳个税", tax))
    print("---------------------")
    money = income_insurace - tax
    total = money + insurance_private + insurance_enterprise
    print("税后收入:", money)
    print("------------------------------------------")

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

# Functions defined below
def get_input_args():
    # Creates parse
    parser = argparse.ArgumentParser()

    parser.add_argument('--base_limit', type=int, default=base_money_limit,
                        help='社保及公积金基数:')

    # returns parsed argument collection
    return parser.parse_args()

main()
