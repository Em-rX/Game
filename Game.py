# Rock ,paper ,scissor or Snake ,water ,gun


import random

def game(you):
    find=['Rock','Paper','Scissor']
    comp_choice=random.choice(find)

    print(f"Computer chose ---->{comp_choice}")
    print(f"you chose      ---->{you}")


    # Comparing Computer choice and user choice
    if comp_choice == you:
        return "It's a tie !"
    elif you=='Rock' and comp_choice=='Scissor' or \
         you=='Paper'and comp_choice=='Rock'   or\
         you=='Scissor' and comp_choice=='Paper':
        return '🎆🎇✨ You win 🎆🎇✨'
    
    else:
        return '😫😩 Fuck off , you loose! 😫😩'
    

 # Get players choice
you=input('Choose Rock , Paper or Scissor :').lower().capitalize()

#call game(you) function

if you in ['Rock','Paper','Scissor']:
    a=game(you)
    print(a)

else:
    print('Invalid choice. Please choose rock, paper, or scissors.')


  




