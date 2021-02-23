import random
print('Welcome to Stone|Paper|Scissor')
n = int(input('Enter 1 to play: \n'))
def print_menu():
  print("Enter 1 to select Stone")
  print("Enter 2 to select Paper")
  print("Enter 3 to select Scissor")

User = 0
Computer = 0
dict = {1:'Stone',2:'Paper',3:'Scissor'}
while (User<5 or Computer<5):
  print_menu()
  my_choice = int(input())
  print('I choose {}'.format(dict.get(my_choice1)))
  comp_choice = random.randint(1,3)
  if (comp_choice==1 and my_choice == 3) or (comp_choice==3 and my_choice == 2) or (comp_choice==2 and my_choice == 1):
    print('Yes!!! I win this round')
    Computer+=1
  else:
    print('Uggh!! I lost this round')
    User+=1
  #print(greet)
  print('---Scores---')
  print('User: {}'.format(User))
  print('Computer: {}'.format(Computer))
  print('------------')
  if User==5:
    print("You won the match, I'll see you next time.")
    break
  elif Computer==5:
    print('I won the match.')
    break