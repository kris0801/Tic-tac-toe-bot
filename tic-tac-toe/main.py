'''Main script'''


import utils
def main(): 
    name = 'KRIS'
    player_id = utils.register(name)
    print (player_id)

    my_turn = utils.is_my_turn(player_id)
    print (my_turn)

if __name__ == '__main__':
    main()