from wos import WosClient
import wos.utils

def print_hi(name):
    with WosClient('eugene.miller@colorado.edu', 'F+KB;!zkfKN7F:') as client:
        print(wos.utils.query(client, 'AU=Knuth Donald'))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
