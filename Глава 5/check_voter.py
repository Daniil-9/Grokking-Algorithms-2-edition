voted = {}

def check_voter(name):
    if name in voted:
        print("Выгнать его!")
    else:
        voted[name] = True
        print("Допустить к голосованию!")

check_voter("Tom")
check_voter("Dan")
check_voter("Dan")
