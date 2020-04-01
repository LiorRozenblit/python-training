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


def cash_withdrawal():
    cash_to_withdrawal = input("please enter amount of money you want to withdrawal:")
    try:
        a = int(cash_to_withdrawal)
        b = int(customer["balance"])
        c = b - a
        customer["balance"] = c
        print('you withdrawal {} money'.format(cash_to_withdrawal))
        return customer["balance"]
    except:
        return customer["balance"]


def cash_deposit():
    cash_to_deposit = input("please enter amount of money you want to deposit:")
    try:
        a = int(cash_to_deposit)
        b = int(customer["balance"])
        c = b + a
        customer["balance"] = c
        print('you deposit {} money'.format(cash_to_deposit))
        return customer["balance"]
    except:
        return customer["balance"]


def change_password():
    new_password = input("please enter new password:")
    print('your new password is {}'.format(new_password))
    customer["password"] = new_password
    return customer["password"]


def main(customer_id):
    atm_password = input("please enter your ATM password:")
    while atm_password != customer["password"]:
        atm_password = input("please enter your ATM password:")
    while customer_id != "-1":
        customer_action = input(
            "please choose between the actions: change password, cash deposit, cash withdrawal, check balance:")
        if customer_action == "change password":
            change_password()
        if customer_action == "cash deposit":
            cash_deposit()
        if customer_action == "cash withdrawal":
            cash_withdrawal()
        if customer_action == "check balance":
            check_balance()
        customer_id = input("please enter -1 if you want to close ATM:")


if __name__ == '__main__':
    main(customer_id)
