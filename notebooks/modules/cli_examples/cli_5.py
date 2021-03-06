import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A program that reads/write from csv and to a txt file')
    parser.add_argument('url', help='The URL to process')
    parser.add_argument('-d', '--destination', help='The name of the file to store the url in')

    args = parser.parse_args()
    print('URL:', args.url)
    print('Destination:', args.destination)
