from gc import collect

from art import logo
import random
import os
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealers = []
players = []
for card in range(4):
    if card % 2 == 0:
        dealers.append(cards[random.randint(0, len(cards) - 1)])
    else:
        players.append(cards[random.randint(0, len(cards) - 1)])

def check_draw(collection_of_cards):
    """ check if the card's total is greater than 21 """
    collection_of_cards = sum(collection_of_cards)
    if collection_of_cards > 21:
        return False
    else:
        return True

def check_ace(collection_of_cards):
    """ check the ace cards (11) if it is needed and convert it into 1 """
    card_sum = sum(collection_of_cards)
    if card_sum > 21:
        for num in collection_of_cards:
            if num == 11:
                collection_of_cards.remove(num)
                collection_of_cards.append(1)
        return collection_of_cards
    else:
        return collection_of_cards

def check_scores(player_cards, dealer_cards, is_player_busted = False, is_dealer_busted = False, is_game_over = False):
    """ check the scores of the game """
    player_sum = sum(player_cards)
    dealer_sum = sum(dealer_cards)
    print(f"      Your current cards {player_cards}, current score: {player_sum}")
    print(f"      Computer's first card: {dealer_cards[0]}\n")

    def print_final_score(player_final,dealer_final,player_sum_final,dealer_sum_final):
        """ print the final score """
        print(f"      Your final hand: {player_final}, final score: {player_sum_final}")
        print(f"      Computer's final hand: {dealer_final}, final score: {dealer_sum_final}\n")

    dealers = []
    players = []
    for card in range(4):
        if card % 2 == 0:
            dealers.append(cards[random.randint(0, len(cards) - 1)])
        else:
            players.append(cards[random.randint(0, len(cards) - 1)])
    if is_player_busted:
        print_final_score(player_cards,dealer_cards,player_sum,dealer_sum)
        print("You went over. You lose 😭")
        blackjack(players,dealers)
    if is_dealer_busted:
        print_final_score(player_cards,dealer_cards,player_sum,dealer_sum)
        print("Computer went over. You win 😁")
        blackjack(players,dealers)
    if not is_player_busted and not is_player_busted and is_game_over:
        if player_sum > dealer_sum:
            print_final_score(player_cards,dealer_cards,player_sum,dealer_sum)
            print("You win 😁")
            blackjack(players,dealers)
        elif player_sum < dealer_sum:
            print_final_score(player_cards, dealer_cards, player_sum, dealer_sum)
            print("You lose 😭")
            blackjack(players, dealers)
        else:
            print_final_score(player_cards, dealer_cards, player_sum, dealer_sum)
            print("Its a draw 😊")
            blackjack(players,dealers)

def dealer(dealers_cards):
    sum_dealer = sum(dealers_cards)
    while sum_dealer < 18:
        dealers_cards.append(cards[random.randint(0, len(cards) - 1)])
        dealers_cards = check_ace(dealers)
        sum_dealer = sum(dealers_cards)
    return dealers_cards

def blackjack(players_card,dealers_card):
    play_a_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n':\n")
    if play_a_game == "y":
        os.system("cls")
        print(logo)
        dealers_card = check_ace(dealers_card)
        check_scores(players_card, dealers_card)
        draw_card = True
        while draw_card:
            draw_another_card = input("Type 'y' to get another card, type 'n' to pass:\n")
            if draw_another_card == 'y':
                players_card.append(cards[random.randint(0, len(cards) - 1)])
                players_card = check_ace(players_card)
                draw_card = check_draw(players_card)
                check_scores(players_card, dealers_card)
                if sum(players_card) > 21:
                    draw_card = False
                    check_scores(players_card, dealers_card, is_player_busted=True)
            else:
                players_card = check_ace(players_card)
                dealers_card = dealer(dealers_card)
                if sum(dealers_card) > 21:
                    check_scores(players_card, dealers_card, is_dealer_busted=True)
                else:
                    check_scores(players_card, dealers_card, is_game_over=True)
                draw_card = False
blackjack(players,dealers)