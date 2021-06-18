def calculate_tuition():
    number_weeks = 5
    rate_increase = .03
    current_tuition = 8000
    print('Year     Projected Tuition (per Semester)')
    print('-----------------------------------------')
    for i in range(1, (number_weeks + 1)):
        current_tuition = current_tuition * rate_increase + current_tuition
        print(f'{i}        ${"{:,.2f}".format(current_tuition)}')


if __name__ == "__main__":
    calculate_tuition()
