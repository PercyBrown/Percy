from game import *
import random

def main():
    while True:
        print('---------------------------------------------------------------------')
        print("Welcome to the Cheater's Tavern - The Human-Computer Battle Version")
        print('---------------------------------------------------------------------')
        print('enter 1 to start the game')
        print('enter 2 to see the rules')
        enter_num = input()
        if enter_num == '1':
            break
        elif enter_num == '2':
            print_rules()
            continue
        else:
            print('Invalid input, please enter 1 or 2.')


    human = HumanPlayer()
    ai = AIPlayer()

    magazine = load_gun()
    magazine_index = 0

    if random.choice([True, False]):  # Choose the first player randomly.
        current_player = human
        next_player = ai
    else:
        current_player = ai
        next_player = human
    print()

    round_num = 1
    while human.alive and ai.alive:
        print()
        print(f"Round {round_num}")
        specified = get_this_round_specified()#Specified card
        print(f'Specified card for this round is {specified}')
        shuffled_cards = cards_shuffler()#shuffled cards
        human.receive_cards(deal_cards_for_human(shuffled_cards))
        ai.receive_cards(deal_cards_for_ai(shuffled_cards))
        print(f"{current_player.name} drops the cards first.")

        while True:
            is_doubt = False
            selected_cards = current_player.play_cards()
            if_trust = next_player.whether_trust(current_player.name, len(selected_cards),len(current_player.cards))
            if if_trust:
                current_player, next_player = next_player, current_player
                continue
            else:
                is_doubt = True
                if if_lie(selected_cards,specified):
                    print(f'{next_player.name} made the correct judgment')
                    pull_trigger(current_player,magazine,magazine_index)
                else:
                    print(f'{next_player.name} made the wrong judgment')
                    pull_trigger(next_player,magazine,magazine_index)
                current_player, next_player = next_player, current_player
                magazine_index += 1

            if check_victory(human, ai):
                return
            if not is_doubt:
                continue
            else:
                round_num += 1
                break

if __name__ == '__main__':
    main()







