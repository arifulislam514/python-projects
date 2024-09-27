import time


def boil_water():
    print("Boiling water...")
    time.sleep(3)
    print("Water boiled!")


def brew_tea():
    print("Adding tea bag to hot water...")
    time.sleep(2)
    print("Steeping the tea...")
    time.sleep(3)
    print("Tea is ready!")


def pour_tea():
    print("Pouring tea into cup...")
    time.sleep(2)
    print("Tea is served!")


def make_tea():
    boil_water()
    brew_tea()
    pour_tea()

# Calling the function to make tea


make_tea()
