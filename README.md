# Mini-project description - Blackjack

Blackjack is a simple, popular card game that is played in many casinos. Cards in Blackjack have the following values: an ace may be valued as either 1 or 11 (player's choice), face cards (kings, queens and jacks) are valued at 10 and the value of the remaining cards corresponds to their number. During a round of Blackjack, the players plays against a dealer with the goal of building a hand (a collection of cards) whose cards have a total value that is higher than the value of the dealer's hand, but not over 21. (A round of Blackjack is also sometimes referred to as a hand.)

The game logic for oursimplified version of Blackjack is as follows. The player and the dealer are each dealt two cards initially with one of the dealer's cards being dealt faced down (his hole card). The player may then ask for the dealer to repeatedly "hit" his hand by dealing him another card. If, at any point, the value of the player's hand exceeds 21, the player is "busted" and loses immediately. At any point prior to busting, the player may "stand" and the dealer will then hit his hand until the value of his hand is 17 or more. (For the dealer, aces count as 11 unless it causes the dealer's hand to bust). If the dealer busts, the player wins. Otherwise, the player and dealer then compare the values of their hands and the hand with the higher value wins. The dealer wins ties in our version.

## Mini-project development process

We suggest you develop your Blackjack game in two phases. The first phase will concentrate on implementing the basic logic of Blackjack while the second phase will focus on building a more full-featured version. In phase one, you will use buttons to control the game and print the state of the game to the console using print statements. In the second phase, you will replace the print statements by drawing images and text on the canvas and add some extra game logic.

## Phase one

1. Implement the methods __𝚒𝚗𝚒𝚝__, __𝚜𝚝𝚛__, 𝚊𝚍𝚍_𝚌𝚊𝚛𝚍 for the 𝙷𝚊𝚗𝚍 class. We suggest modeling a hand as a list of Card objects that are stored in a field in the Hand object. The __𝚒𝚗𝚒𝚝__ method should initialize the Hand object to have an empty list of Card objects. The 𝚊𝚍𝚍_𝚌𝚊𝚛𝚍 should append a Card object to this list of cards. The __𝚜𝚝𝚛__ method should return a string representation of a Hand object in a human-readable form.For help in implementing the __𝚜𝚝𝚛__ method, refer back to the solution to question four in the Practice Exercises for week 5a. Remember to use the string method for Card objects to convert each card in the hand's list of cards into a string. (Don't convert a Card object into a string in 𝚊𝚍𝚍_𝚌𝚊𝚛𝚍 to make your string method work.)

2. Implement the methods for the 𝙳𝚎𝚌𝚔 class listed in the mini-project template. We suggest modeling a deck of cards as list of cards. You can generate this list using a pair of nested 𝚏𝚘𝚛 loops or a list comprehension. Remember to use the 𝙲𝚊𝚛𝚍 initializer to create your cards. Use 𝚛𝚊𝚗𝚍𝚘𝚖.𝚜𝚑𝚞𝚏𝚏𝚕𝚎() to shuffle this deck of cards.Remember that the deck is randomized after shuffling, so the output of the testing template should match the output in the comments in form but not in exact value.

3. Implement the handler for a "Deal" button that shuffles the deck and deals the two cards to both the dealer and the player. The event handler 𝚍𝚎𝚊𝚕 for this button should shuffle the deck (stored as a global variable), create new player and dealer hands (stored as global variables), and add two cards to each hand. To transfer a card from the deck to a hand, you should use the 𝚍𝚎𝚊𝚕_𝚌𝚊𝚛𝚍 method of the 𝙳𝚎𝚌𝚔 class and the 𝚊𝚍𝚍_𝚌𝚊𝚛𝚍 method of 𝙷𝚊𝚗𝚍 class in combination. The resulting hands should be printed to the console with an appropriate message indicating which hand is which.

4. Implement the 𝚐𝚎𝚝_𝚟𝚊𝚕𝚞𝚎 method for the 𝙷𝚊𝚗𝚍 class. You should use the provided 𝚅𝙰𝙻𝚄𝙴 dictionary to look up the value of a single card in conjunction with the logic explained in the video lecture for this project to compute the value of a hand.

5. Implement the handler for a "Hit" button. If the value of the hand is less than or equal to 21, clicking this button adds an extra card to player's hand. If the value exceeds 21 after being hit, print "You have busted".

6. Implement the handler for a "Stand" button. If the player has busted, remind the player that they have busted. Otherwise, repeatedly hit the dealer until his hand has value 17 or more (using a while loop). If the dealer busts, let the player know. Otherwise, compare the value of the player's and dealer's hands. If the value of the player's hand is less than or equal to the dealer's hand, the dealer wins. Otherwise the player has won. Remember the dealer wins ties in our version.

## Phase two 

1. Implement your own 𝚍𝚛𝚊𝚠 method for the 𝙷𝚊𝚗𝚍 class using the 𝚍𝚛𝚊𝚠 method of the 𝙲𝚊𝚛𝚍 class. We suggest drawing a hand as a horizontal sequence of cards where the parameter 𝚙𝚘𝚜 is the position of the upper left corner of the leftmost card. To simplify your code, you may assume that only the first five cards of a player's hand need to be visible on the canvas.

2. Replace printing in the console by drawing text messages on the canvas. We suggest adding a global 𝚘𝚞𝚝𝚌𝚘𝚖𝚎 string that is drawn in the draw handler using 𝚍𝚛𝚊𝚠_𝚝𝚎𝚡𝚝. These messages should prompt the player to take some require action and have a form similar to "Hit or stand?" and "New deal?". Also, draw the title of the game, "Blackjack", somewhere on the canvas.

3. Add logic using the global variable 𝚒𝚗_𝚙𝚕𝚊𝚢 that keeps track of whether the player's hand is still being played. If the round is still in play, you should draw an image of the back of a card over the dealer's first (hole) card to hide it. Once the round is over, the dealer's hole card should be displayed.

4. Add a score counter that keeps track of wins and losses for your Blackjack session. In the simplest case, the program displays wins minus losses. However, you are welcome to implement a more sophisticated betting/scoring system. 

5. Modify the logic for the "Deal" button to create and shuffle a new deck (or restock and shuffle an existing deck) each time the "Deal" button is clicked. This change avoids the situation where the deck becomes empty during play.

6. Finally, modify the 𝚍𝚎𝚊𝚕 function such that, if the "Deal" button is clicked during the middle of a round, the program reports that the player lost the round and updates the score appropriately. 

