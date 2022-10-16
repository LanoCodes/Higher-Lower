from art import logo, vs
from game_data import data
from replit import clear
import random as r



# i think there is a way to make this solution recursive. I want to choose that option because I think it might be a very straightforward way of persistent the correctly chose higher insta acct towards the next comparison
def InstaAcctGen():
  """Returns a random istagram acount that has it's own data in the form of a dictionary."""
  return data[r.randint(0, len(data) - 1)]

def HigherOrLower(acct1, acct2, score):
  """Compares instagram accounts for the highest follower count"""
  # print out the program logo
  print(logo)
  if score != 0:
    print(f"You got it right! Current Score: {score}")
    
  print(f"Compare A: {acct1['name']}, a {acct1['description']}, from {acct1['country']}")
  print(vs)
  print(f"Against B: {acct2['name']}, a {acct2['description']}, from {acct2['country']}")

  # ask the user what account they think has more followers
  user_account_choice = input("Which account has more followers? Type 'A', or 'B': ")
  # if the user inputted 'A' then their choice has to tracked to acct1, if input was 'B', then their choice has to be tracked to acct2
  if user_account_choice == 'A':
    # user_account_choice = acct1['follower_count']
    user_account_choice = acct1
    account_followers_compared_to = acct2['follower_count']
  else:
    user_account_choice = acct2
    account_followers_compared_to = acct1['follower_count']
  # is the account that the user chose >  account to be compared against?
  #  if so: congratulate user, increment their score, then pass that account back into this function along with a newly generated acct for another comparison to made. clear the screen
  if user_account_choice['follower_count'] >= account_followers_compared_to:
    score += 1
    clear()
    HigherOrLower(user_account_choice, InstaAcctGen(), score)
  # if not: return a message to the user saying, that wasn't correct and show them their final score
  else:
    clear()
    print(f"Yea :/...that choice wasn't right. Final score: {score}")
    return False

score = 0

HigherOrLower(InstaAcctGen(), InstaAcctGen(), score)
  
# a while loop that keeps repeating until winning flag is False
# asking the user to pick between choice A or B, maybe some error handling there for instances of lowercase inputs
# Sentence formatting of the data for the choices that makes sense.
# a patterned way to get the same sentence structure from eawc
# so flag that tracks that the user is winning still
# a vs logo between the two choices
#  a point tracker 
# text to display points when user loses

