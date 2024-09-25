import random
MAX_LINES = 3
MIN_BET = 10
MAX_BET = 5000
ROW = 3
COLUMN = 3
symbols = {
    'A' : 2,
    'B' : 4,
    'C' : 6,
    'D' : 8
}
symbols_values = {
    'A' : 5,
    'B' : 4,
    'C' : 3,
    'D' : 8
}
class Guess:
    def __init__(self):
        self.amount = 0
        self.bet = 0
        self.lines = 0

    def get_slot_machine_spin(self, rows, cols, symbols):
        self.all_symbols = []
        for symbol, symbol_count in symbols.items():
            for _ in range(symbol_count):  # when you don't need variable in loop, start like for _ in .....
                self.all_symbols.append(symbol)
        
        self.columns = []
        for _ in range(cols):
            self.column = []
            self.current_symbol = self.all_symbols[:]  # to copy the all_symbol, like choose by value not by reference
            for _ in range(rows):
                value = random.choice(self.current_symbol)
                self.column.append(value)
                self.current_symbol.remove(value)
            
            self.columns.append(self.column)  
        
        return self.columns
    
    def check_winnings(self, columns, lines, bet, values):
        self.winnings=0
        self.winnings_lines = []
        for line in range(lines):
            self.symb = columns[0][line]
            self.win_line = True
            for column in columns:
                self.symbol_check = column[line]
                if self.symb != self.symbol_check:
                    self.win_line=False
                    break
                
            if self.win_line:
                self.winnings += values[self.symb] * bet
                self.winnings_lines.append(line + 1)
                    
        return self.winnings, self.winnings_lines
    
    def print_slot_machine(self, columns):
        for row in range(len(columns[0])):
            for i, column in enumerate(columns):
                if i != len(columns) - 1:
                    print(column[row], end=" | ")  
                else:
                    print(column[row])  
        
    def deposit(self):
        while True:
            self.amount = input("Enter Amount You want to deposit : $")
            if self.amount.isdigit():
                self.amount = int(self.amount)
                if self.amount > 0:
                    break
                else:
                    print("Please enter Amount greater than 0.")
            else:
                print("Please Enter Digit.")    
        return self.amount
                
    def get_Bet(self):
        while True:
            self.bet = input("Enter Amount You want to bet : $")
            if self.bet.isdigit():
                self.bet = int(self.bet)
                if MIN_BET <= self.bet <= MAX_BET :
                    break
                elif self.bet > MAX_BET:
                    print(f"Please enter Amount less than {MAX_BET}.")
                elif self.bet < MIN_BET:
                    print(f"Please enter Amount greater than {MIN_BET}.")
            else:
                print("Please Enter Digit.")    
        return self.bet
                
    def number_of_Lines(self):
        while True:
            self.lines = input(f"Enter lines You want to bet on from 1 to {MAX_LINES} : ")
            if self.lines.isdigit():
                self.lines = int(self.lines)
                if 1 <= self.lines <= MAX_LINES :
                    break
                else:
                    print("Please enter Line number between 1 and 3.")
            else:
                print("Please Enter Digit.")    
                
        return self.lines
  
    def game(self,balance):
        self.lines = self.number_of_Lines()
        while True:
            self.bet = self.get_Bet()
            self.total_bal = self.bet*self.lines
            if self.total_bal > balance:
                print(f"You do not have enough Balance to bet.\nYour Balance is {balance}")
            else:
                break
       
        print(f"total bet = ${self.total_bal}")
        self.slots = self.get_slot_machine_spin(ROW, COLUMN, symbols)
        self.print_slot_machine(self.slots)
        self.winnings, self.winning_lines = self.check_winnings(columns=self.slots, bet=self.bet, lines= self.lines, values=symbols_values)
        print(f"You won {self.winnings}")
        if self.winnings > 0:
            print(f"You won on : ", *self.winning_lines) # * is here splat operator or unpack operator 
        return self.winnings - self.total_bal
  
  
  
def main():
    man = Guess()
    balance = man.deposit()
    while True:
        print(f'Current Balance is {balance}')
        spin = input('press Enter to start the Game ( Q to quit).').lower()
        if spin == 'q':
            break
        balance_change = man.game(balance=balance)
        balance += balance_change
        if balance <= 0:
            print("You have no more balance left. Game over.")
            break
        
main()