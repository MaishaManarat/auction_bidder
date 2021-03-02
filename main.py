from os import system, name

# For clearing screen after every bidding input
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


from art import logo

print(logo)
print("Welcome to the secret auction program!!")

biding_list = []
biding_dic = {}

print("what is your name? ")
name = input()
print("How much do you want to bid? ")
bid = int(input())
biding_dic[name] = bid


print("Are there other bidders? Type yes or no")
option = input()




while option != "no":
  clear()
  print("what is your name? ")
  name = input()
  print("How much do you want to bid? ")
  bid = int(input())
  print("Are there other bidders? Type yes or no")
  option = input()
  biding_dic[name] = bid

clear()

win = ''
a = 0
for key in biding_dic:
  if a < biding_dic[key]:
    a = biding_dic[key]
    win = key

#print(biding_dic)
print(f"The winner of the bid is {win} of {a}$")
