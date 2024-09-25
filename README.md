# Slot Machine Betting Game
The Slot Machine Betting Game is a Python-based console application that simulates a classic slot machine experience. Players can deposit money, place bets on multiple lines, and spin the slot machine to win or lose money based on symbol combinations. The game uses a randomization algorithm to generate the slot outcomes .

## Key Features: 
Deposit System:
  The player starts by depositing a desired amount of money into the game, ensuring the balance is greater than zero.

Bet Placement:
  Players can bet on 1 to 3 lines of the slot machine with adjustable bet amounts.
The bet amount must be within a minimum of $10 and a maximum of $5000, providing flexibility for low and high-stakes players.

Slot Machine Mechanics:
  The game features a 3x3 grid of symbols where each column contains randomly chosen symbols.
Symbols include 'A', 'B', 'C', and 'D', each with unique probabilities and corresponding payout values.

Winning Calculation:
  After each spin, the game checks if the symbols in a line are the same across all columns.
Winnings are calculated based on the symbol value and the player's bet amount.
The player is informed about the lines they've won on, and the balance is updated accordingly.

User Interaction:
  The user can continue playing by placing additional bets or quit the game when they run out of balance or choose to stop.
