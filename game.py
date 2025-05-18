import random



class HumanPlayer:
    def __init__(self):
        self.name = 'You'
        self.cards = []
        self.alive = True

    def receive_cards(self, cards):
        self.cards = cards

    def play_cards(self):#Choose the cards to be played
        print(f"Your cards are：{self.cards}")
        while True:
            try:
                choose_index = input(
                    "Select the card index (start from 1) to be displayed (up to 2, separated by spaces): ").split()
                if not 1 <= len(choose_index) <= 2:
                    print("You must choose 1 - 2 cards.")
                    continue

                choose_index = [int(i) - 1 for i in choose_index]

                if any(i < 0 or i >= len(self.cards) for i in choose_index):
                    print("Invalid index. Please try again.")
                    continue

                selected_cards = [self.cards[i] for i in choose_index]
                for i in sorted(choose_index,reverse=True):
                    del self.cards[i]
                break
            except Exception as e:
                print("Error input. Please select again.")
        return selected_cards

    def whether_trust(self, AI_name, num_cards,remain_cards):#Decide whether to trust or not
        if remain_cards == 0:
            print(f'{AI_name} dropped {num_cards} cards,{AI_name} has no cards left,so you have to doubt it.')
            return False
        while True:
            trust = input(f"{AI_name} dropped {num_cards} cards,do you trust it? (y/n): ").strip().lower()
            if trust == 'y':
                return True
            elif trust == 'n':
                return False
            else:
                print('Error input. Please choose again.')
                continue


class AIPlayer:
    def __init__(self):
        self.name = "AIPlayer"
        self.cards = []
        self.alive = True

    def receive_cards(self, cards):
        self.cards = cards

    def play_cards(self):
        count = random.choice([1, 2]) if len(self.cards) >= 2 else 1
        selected = random.sample(self.cards, count)
        for i in selected:
            self.cards.remove(i)
        return selected

    def whether_trust(self, your_name, num_cards,remain_cards):#Decide whether to trust or not randomly
        trust = random.choice([True, False])
        if remain_cards == 0:
            print(f'{your_name} dropped {num_cards} cards,{your_name} has no cards left,so {self.name} have to doubt you.')
            trust = False
        if_trust = 'trust' if trust else 'doubt'
        print(f"{your_name} dropped {num_cards} cards,AIPlayer {if_trust} you.")
        return trust


def get_this_round_specified():
    specified = random.choice(['K', 'Q', 'A'])
    return specified

def cards_shuffler():
    cards = ['K'] * 6 + ['Q'] * 6 + ['A'] * 6
    random.shuffle(cards)
    return cards

def deal_cards_for_human(shuffled_cards):
    return shuffled_cards[:5]

def deal_cards_for_ai(shuffled_cards):
    return shuffled_cards[5:10]

def load_gun():
    magazine = [False] * 6
    bullet_pos = random.randint(0, 5)
    magazine[bullet_pos] = True
    return magazine

def pull_trigger(player,magazine,magazine_index):
    print(f"{player.name} pulls the trigger.", end=' ')
    if magazine[magazine_index]:
        print("Bang! Shot!")
        player.alive = False
    else:
        print("Click... No bullet.")

def if_lie(selected_cards, specified):
    for i in selected_cards:
        if i != specified:
            return True
    return False


def check_victory(p1, p2):
    if not p1.alive:
        print(f"\nGame over, {p2.name} wins!")
        return True
    if not p2.alive:
        print(f"\nGame over, {p1.name} wins!")
        return True
    return False

def print_rules():
    print("Rules:")
    print('''
    Card pool: 6 K cards, 6 Q cards, 6 A cards
    In each round, randomly select one K/Q/A card as the "specified card"
    There are two players, one of whom is a player and the other is a computer
    Start with a 6-round revolver pistol, with only 1 bullet (in the form of roulette)
    Each round sequence: Player 1 drops 1 - 2 face-down cards and declares them as the "specified card"
    Player 2 can choose to "believe" or "doubt"
    If the doubt is successful, Player 1 shoots himself; otherwise, Player 2 shoots himself
    If someone dies, the game ends; if not, the game continues by reshuffling the cards
    If "believed", it's Player 2's turn to drop
    Repeat the above sequence
    After each shot, the turn changes to the other player to drop first 
    Game ends after someone being hit once. 
    If one player finishes playing their cards first, the other player must doubt. 
    The player who survives in the end wins.
    ''')