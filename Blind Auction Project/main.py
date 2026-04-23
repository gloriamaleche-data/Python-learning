import art
print(art.logo)
# TODO-1: Ask the user for input
print('Welcome to Texas Bidders!')

empty_dict = {}
continue_bidding = True
while continue_bidding:
    name = input('What is your name? ')
    bid_amt = int(input('How much would you like to bid? $'))
    quest = input('Are there any other bidders? Type \'yes\' or \'no\':\n ')
    print('\n'*100)

    empty_dict[name] = bid_amt

    if quest == 'no':
        continue_bidding = False
save_largest_value = 0
winner = ''
for key in empty_dict:
    if empty_dict[key] > save_largest_value:
        save_largest_value = empty_dict[key]
        winner = key

print(f'The highest bidder is {winner} with a bid of ${save_largest_value}')




