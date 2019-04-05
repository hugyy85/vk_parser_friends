from operations import main
from config import nickname
from queries import *
from time import time


if __name__ == '__main__':
    start = time()
    main(nickname)
    write_result_to_file('city', how_many_cities())
    write_result_to_file('country', how_many_country())
    write_result_to_file('friends', how_many_friends_of_your_friends())
    write_result_to_file('contacts', get_all_contacts())
    write_result_to_file('names', how_many_names())
    end = time()
    with open('time.txt', 'w') as f:
        try:
            f.write(str(round((end-start)/3600, 2)) + ' hours takes it is programm')
        except:
            pass






