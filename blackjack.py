import collections
import random
import time

Card = collections.namedtuple('Card', ['rank', 'suit']) # does this come with a copy method?

class Deck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self.cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]
    
    def __getitem__(self, position):
        return self.cards[position]

    def shuffle(self):
        random.shuffle(self.cards)

class BlackJack:

    def __init__(self, shuffled_deck):
        self._deck = shuffled_deck
        self.player_hand = []
        self.dealer_hand = []
        self.location = 0

    def __call__(self):
        player_in = True
        tie = False
        dealer_in = True
        while dealer_in:
            player_in = self.player_turn()
            if not player_in:
                break
            dealer_in = self.dealer_turn()
            if self.calc_value(self.player_hand) == self.calc_value(self.dealer_hand) and self.calc_value(self.player_hand) == 21:
                tie = False
                break
        time.sleep(1) 
        if player_in:
            print(f'Congratulations! You won {self.calc_value(self.player_hand)} against {self.calc_value(self.dealer_hand)}')
        elif tie:
            print(f'Wow...You tied {self.calc_value(self.player_hand)} to {self.calc_value(self.dealer_hand)}')
        else:
            print(f'Unlucky! You lost {self.calc_value(self.player_hand)} against {self.calc_value(self.dealer_hand)}')
        
    # deals card and increases location by 1
    def deal(self):
        self.location += 1
        return self._deck[self.location - 1] 
    
    def player_turn(self):
        time.sleep(1)
        print(f"Your current hand is {self.player_hand}")
        time.sleep(1) 
        while True:
            choice = input("""
            Enter 1 to hit:
            Enter 0 to hold:
            """)
            if choice == '1':
                self.player_hand.append(self.deal())
                print(f"Your new hand is {self.player_hand}")
                break
            elif choice == '0':
                print('You chose to hold.')
                break
        # now we evaluate scores
        current_player_total = self.calc_value(self.player_hand)
        time.sleep(1) 
        if current_player_total > 21:
            print(f'You lost with {current_player_total}')
            return False
        else:
            print(f'Your current score is {current_player_total}')
            return True
    
    def dealer_turn(self):
        time.sleep(1)
        print(f"The dealer's current hand is: {self.dealer_hand}")
        time.sleep(1) 
        if self.calc_value(self.dealer_hand) < 19:
            self.dealer_hand.append(self.deal())
            print('The dealer decides to hit.')
            time.sleep(1) 
            print(f"The dealer's new hand is: {self.dealer_hand}.")
        elif self.calc_value(self.player_hand) > self.calc_value(self.dealer_hand):
            self.dealer_hand.append(self.deal())
            print('The dealer decides to hit.')
            time.sleep(1) 
            print(f"The dealer's new hand is: {self.dealer_hand}.")
        else:
            print('The dealer chooses to hold.')
        # now we evaluate scores   
        time.sleep(1)  
        current_dealer_total = self.calc_value(self.dealer_hand)
        if current_dealer_total > 21:
            print(f'The dealer lost with {current_dealer_total}.')
            return False
        else:
            print(f"The dealer's current score is {current_dealer_total}.")
            return True
    
    # want to sort the hand in the way that is the best for the user, so we will count Aces last
    def sort_hand(self, hand):
        return [card for card in hand if card.rank != 'A'] + [card for card in hand if card.rank == 'A']
    
    def calc_value(self, hand):
        tot = 0
        sorted_hand = self.sort_hand(hand)
        for card in sorted_hand:
            if card.rank in list('JQK'):
                tot += 10
            elif card.rank == 'A':
                if tot + 11 > 21:
                    tot += 1
                else:
                    tot += 11
            else: # should be a number in this case
                tot += int(card.rank)
        return tot


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()

    bj = BlackJack(deck)
    bj()


