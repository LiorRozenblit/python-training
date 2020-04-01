import sys
customer = {"password": 0, "balance": 0}
input_file = sys.argv[1]
my_list = []
read = open(input_file, 'r')
Count = 0
for line in read:
    for word in line.split():
        my_list.append(word)
        Count += 1
read.close()
customer_id = input("please enter your customer id:")
for i in range(Count):
    if customer_id == my_list[i]:
        customer["balance"] = my_list[i + 1]
        customer["password"] = my_list[i + 2]


def check_balance():
    print('you have {} money in your balance'.format(customer["balance"]))
    return customer["balance"]


def cash_withdrawl():
    cash_to_withdrawl = input("please enter amount of money you want to withdrawl:")
    print('you withdrawl {} money'.format(cash_to_withdrawl))
    customer["balance"] -= cash_to_withdrawl
    return customer["balance"]


def cash_deposit():
    cash_to_deposit = input("please enter amount of money you want to deposit:")
    print('you deposit {} money'.format(cash_to_deposit))
    customer["balance"] += cash_to_deposit
    return customer["balance"]


def change_password():
    new_password = input("please enter new password:")
    print('your new password is {}'.format(new_password))
    customer["password"] = new_password
    return customer["password"]


def main():
    atm_password = input("please enter your ATM password:")
    while atm_password != customer["password"]:
        atm_password = input("please enter your ATM password:")
    while customer_id != -1:
        customer_action = input(
            "please choose between the actions: change password, cash deposit, cash withdrawl, check balance:")
        if customer_action == "change password":
            change_password()
        if customer_action == "cash deposit":
            cash_deposit()
        if customer_action == "cash withdrawl":
            cash_withdrawl()
        if customer_action == "check balance":
            check_balance()


if __name__ == '__main__':
    main()
