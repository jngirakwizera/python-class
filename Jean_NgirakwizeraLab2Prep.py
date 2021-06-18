def calculate_pay(hw, pr):
    if hw > 40:
        ot = (hw - 40) * 1.5 * pr
        pay = (40 * pr) + ot
    else:
        ot = 0
        pay = hw * pr
    return ot, pay


def process_pay():
    number_weeks = int(input("Enter number of weeks: "))
    pay_rate = float(input("Enter pay rate:"))
    total_pay = 0
    for i in range(1, (number_weeks + 1)):
        hours = float(input("Enter hours worked: "))
        overtime, pay = calculate_pay(hours, pay_rate)
        print(f'Pay for Week{i} {"is":10} ${pay:.2f}')
        if overtime > 0:
            print(f'{"Overtime pay":24} ${overtime:.2f}')
        total_pay += pay
    print(f'{"Total Pay is ":23} ${total_pay:.2f}')


if __name__ == "__main__":
    process_pay()
