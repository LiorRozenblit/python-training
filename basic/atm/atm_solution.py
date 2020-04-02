import sys
customer = []
input_file = sys.argv[1]
my_list = []
balance = 1
password = 2
number_of_customers = 1
customer_id = ''
read = open(input_file, 'r')
for line in read:
    number_of_customers += 1
    for word in line.split():
        my_list.append(word)
read.close()
for i in range(number_of_customers - 1):
    customer.append({"balance": my_list[balance], "password": my_list[password]})
    balance += 3
    password += 3
customer_id = input("please enter your customer id:")
while not 0 < int(customer_id) < number_of_customers:
    customer_id = input("please enter your customer id:")
atm_password = input("please enter your ATM password:")
while atm_password != customer[int(customer_id) - 1]["password"]:
    atm_password = input("please enter your ATM password:")



def check_balance():
    print('you have {} money in your balance'.format(customer[int(customer_id) - 1]["balance"]))
    return customer[int(customer_id) - 1]["balance"]


def cash_withdrawal():
    cash_to_withdrawal = input("please enter amount of money you want to withdrawal:")
    try:
        a = int(cash_to_withdrawal)
        b = int(customer[int(customer_id) - 1]["balance"])
        c = b - a
        customer[int(customer_id) - 1]["balance"] = c
        print('you withdrawal {} money'.format(cash_to_withdrawal))
        return customer[int(customer_id) - 1]["balance"]
    except:
        return customer[int(customer_id) - 1]["balance"]


def cash_deposit():
    cash_to_deposit = input("please enter amount of money you want to deposit:")
    try:
        a = int(cash_to_deposit)
        b = int(customer[int(customer_id) - 1]["balance"])
        c = b + a
        customer[int(customer_id) - 1]["balance"] = c
        print('you deposit {} money'.format(cash_to_deposit))
        return customer[int(customer_id) - 1]["balance"]
    except:
        return customer[int(customer_id) - 1]["balance"]


def change_password():
    new_password = input("please enter new password:")
    print('your new password is {}'.format(new_password))
    customer[int(customer_id) - 1]["password"] = new_password
    return customer[int(customer_id) - 1]["password"]


def main(customer_id):
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
    write_file = open(input_file, 'w')
    for Count in range(number_of_customers - 1):
        write_file.write(str(Count + 1) + " " + str(customer[Count]["balance"]) + " " + str(customer[Count]["password"]) + "\n")



if __name__ == '__main__':
    main(customer_id)
