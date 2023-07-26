import os
import datetime
import csv
import requests
import random
import threading

def get_formatted_timestamp():
  """Returns a formatted timestamp in the format YYYY-MM-DD HH:MM:SS."""

  now = datetime.datetime.now()
  timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
  return timestamp

def get_status_code(url):
  response = requests.get(url,timeout=2)
  return response.status_code

def append_data_to_csv(data, filename):
  with open(filename, "a") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(data)


def generate_random_ip():
  a = random.randint(1, 255)
  b = random.randint(1, 255)
  c = random.randint(1, 255)
  d = random.randint(1, 255)
  return f"{a}.{b}.{c}.{d}"

def read_csv(filename):
  with open(filename, "r") as csvfile:
      reader = csv.reader(csvfile, delimiter=",")
      for row in reader:
        # lines.append(row)
        append_data_to_csv(row, os.path.join('results', f"{row[0]}.csv"))

def start_crawl():
  while True:
    try:
      url = f"http://{generate_random_ip()}"
      result = get_status_code(url)
      print(result)
      append_data_to_csv([get_formatted_timestamp(), url], os.path.join('results', f"{result}.csv"))
    except Exception as e:
      print(e)

def start_crawl_threaded():
  for i in range(32):
    t = threading.Thread(target=start_crawl)
    t.start()

if __name__ == "__main__":
  # read_csv("result.csv")
  start_crawl_threaded()