import random, sys, time
# List of firework emojis
fireworks = ["🎆", "🎇", "✨", "💥", "🎆", "🎇"]

# Function to create a simple fireworks text animation
def fireworks_animation():
    for i in range(10):  # Loop to create the animation effect
        sys.stdout.write("\r" + random.choice(fireworks) * (i + 1))  # Print fireworks with increasing count
        sys.stdout.flush()
        time.sleep(0.2)  # Pause to create animation effect
    print("\nBoom! 🎆🎇💥")  # Final explosion

jap_nums = {1: 'ICHI', 2: 'NI', 3: 'SAN',
4: 'SHI', 5: 'GO', 6: 'ROKU'}

wallet = 5000
total_top_up = 0
print ('define your threshold for gamling for top ups')
threshold = int(input())

def get_bet(wallet):
    while True:
        print(f'You have {wallet} mon. How much do you bet? OR QUIT')
        bet = input().strip().upper()
        if bet == 'QUIT':
            print('You quit')
            sys.exit()
        elif not bet.isdigit():
            print('Enter a valid number')
            continue
        bet = int(bet)
        if bet > wallet:
            print("You don't have enough money")
            continue
        return bet
    
def get_guess():
    while True:
        print ('Cho (even) or HAN (odd)?')
        guess = input().upper()
        if guess not in ['CHO','HAN']:
            print ("enter CHO or HAN please")
            continue
        return guess

def top_up_wallet():
    global wallet, total_top_up
    while True:
        print("You have no money left. Do you want to top up? (YES/NO)")
        choice = input().strip().upper()
        if choice == 'YES':
            wallet = 0 
            while True:
                print("Enter the amount to top up:")
                amount = input().strip()
                if amount.isdigit() and int(amount) > 0:
                    wallet += int(amount)
                    total_top_up +=int(amount)
                    print(f'Your new wallet balance is {wallet} mon.')
                    check_threshold()
                    return wallet
                else:
                    print("Enter a valid positive number.")
        elif choice == 'NO':
            print("Game over. You quit.")
            sys.exit()
        else:
            print("Enter YES or NO.")
            
def check_threshold():
    global total_top_up, threshold
    if total_top_up >= threshold:
        print(f"Warning! You have topped up {total_top_up} mon, which is above the gambling threshold of {threshold}.")
        print("Be careful not to overdo it!")

def play_game(wallet):
    while True:
        if wallet <= 0:
            
            wallet = top_up_wallet()
        bet = get_bet(wallet)
        guess = get_guess()
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print('The dealer lifts the cup to reveal:')

        print(' ', jap_nums[dice1], '-', jap_nums[dice2])
        print(' ', dice1, '-', dice2)

        rollsIsEven = (dice1+dice2)%2 ==0
        if guess == 'CHO' and rollsIsEven: 
            print ("You won! You take ", str(bet*2))
            print ("The house collects a ",str(bet// 10), "mon fee.")
            wallet = wallet + bet -(bet// 10)
            # Call the display_fireworks function
            fireworks_animation()

        else:
            print ("You lost ",str(bet))
            wallet = wallet - int(bet)
            print(f"You lost {bet} mon. \n")
            print("  _______  ")
            print(" /       \\ ")
            print("|  X   X  | ")
            print("|    >    | ")
            print("|   ---   | ")
            print(" \\_______/ ")
        check_threshold()
play_game(wallet)