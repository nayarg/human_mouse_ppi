import pickle
import argparse

def convert(filepath):
  f = open(filepath, 'rb')
  converted = pickle.load(f)
  return converted

def main(args):
  filepath = args.binary_filepath
  converted_txt = convert(filepath)
  print (converted_txt)


if __name__ == '__main__':
  parser =  argparse.ArgumentParser()
  parser.add_argument('binary_filepath')

  args = parser.parse_args()
  main(args)