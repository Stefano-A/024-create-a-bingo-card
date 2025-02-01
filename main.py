import random

def create_bingo_card():
    bingo_card = {}
    step = 0
    for char in 'BINGO':
        bingo_card.update({char : random.sample(range(1+step, 15+step), k = 5)})
        step += 15
    return bingo_card

def display_card(dict_card):
    print(' B  I  N  G  O')
    
    for i in range(0,5):
        row = list(item[i] 
                    for item in dict_card.values())

        print(f'{row[0]:2d} {row[1]} {row[2]} {row[3]} {row[4]}')
      

x = create_bingo_card()         
display_card(x)