'''Main script'''
from unicodedata import name

import utils
def main(): 
    name = 'KRIS'
    player_id = utils.register(name)

if __name__ == '__main__':
    main()