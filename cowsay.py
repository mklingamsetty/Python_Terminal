import sys
from heifer_generator import HeiferGenerator as HG

def list_cows(COW):
    return " ".join(cow.name for cow in COW)
def find_cow(name, COW):
    return next((cow for cow in COW if cow.name == name), None)
def main(args):

    COW = HG.get_cows()

    match args[1]:

        case "-l":
            print(f"Cows available: {list_cows(COW)} ")

        case "-n":
            cow = find_cow(args[2], COW)

            if cow:
                print(f'\n{" ".join(args[3:])} \n{cow.image}')

                if cow.name == "dragon" or cow.name == "ice-dragon":
                    if cow.can_breathe_fire():
                        print("This dragon can breathe fire.")
                    else:
                        print("This dragon cannot breathe fire.")
            else:
                print(f"Could not find {args[2]} cow!")

        case _:
            print(f'\n{" ".join(args[1:])} \n{COW[0].image}')




if __name__ == "__main__":
    main(sys.argv)



