import multiprocessing

def sec(seconds):
    from datetime import datetime
    
    print( seconds)

if __name__ == "__main__":
    import random
    #setting the 3 processes
    for n in range(3):
        seconds = random.random()
        proc = multiprocessing.Process(target=sec, args=(seconds,))
        proc.start()