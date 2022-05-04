'''Main script'''


import utils
def main(): 
    name = 'KRIS'
    player_id = utils.register(name)
    print (player_id)

if __name__ == '__main__':
    main()