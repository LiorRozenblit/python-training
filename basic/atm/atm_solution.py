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
        customer["password"] = my_list[i+2]
ATM_password = input("please enter your ATM password id:")
if ATM_password == customer["password"]:
    print("true")
else:
    print("false")
print(customer)
