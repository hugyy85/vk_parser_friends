from operations import main
from config import nickname
from queries import *
from time import time


if __name__ == '__main__':
    start = time()
    main(nickname)
    how_many_country()
    how_many_cities()
    end = time()
    with open('time.txt', 'w') as f:
        try:
            f.write(str(round((end-start)/3600, 2)) + ' hours takes it is programm')
        except:
            pass






