'''Main script'''


import utils
import time 
def main(): 
    name = 'KRIS'
    player_id = utils.register(name)
    print (player_id)

    my_turn = utils.is_my_turn(player_id)

    while not my_turn:
        print ('zzz...')
        time.sleep(3)
        my_turn = my_turn = utils.is_my_turn(player_id)
    print('continue in game')

if __name__ == '__main__':
    main()