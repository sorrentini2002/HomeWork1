# -*- coding: utf-8 -*-
"""codici_homework1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ePYiFr7Y_8mY1OFUbkholhIP0MIt_pUx
"""

# Say "Hello, World!" With Python
if __name__ == '__main__':
    print("Hello, World!")

# Python If-Else
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n%2!=0:
        print("Weird")
    else:
        if n>=2 and n<5:
            print("Not Weird")
        else:
            if n>=6 and n<=20:
                print("Weird")
            else:
                print("Not Weird")

# Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(a+b)
    print(a-b)
    print(a*b)

# Python: Division

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

# Loops

if __name__ == '__main__':
    n = int(input())
    i = 0
    while i < n:
        print(i**2)
        i += 1

# Write a function

def is_leap(year):
    leap = False

    # Write your logic here


    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                leap = True
        else:
            leap = True
    return leap


year = int(input())
print(is_leap(year))

# Print Function

if __name__ == '__main__':
    n = int(input())

    for i in range(1, n + 1):
        print(i, end = "")

# Lists

if __name__ == '__main__':
    N = int(input())
    lst = []
    for _ in range(N):
        command = input().split()
        if command[0] == "insert":
            lst.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(lst)
        elif command[0] == "remove":
            lst.remove(int(command[1]))
        elif command[0] == "append":
            lst.append(int(command[1]))
        elif command[0] == "sort":
            lst.sort()
        elif command[0] == "pop":
            lst.pop()
        elif command[0] == "reverse":
            lst.reverse()

# sWAP cASE

def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# String Split and Join

def split_and_join(line):
    return "-".join(line.split())

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# What's Your Name?

#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

# Mutations

def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# Find a string

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

# String Validators

if __name__ == '__main__':
    s = input()
    print(any(char.isalnum() for char in s))
    print(any(char.isalpha() for char in s))
    print(any(char.isdigit() for char in s))
    print(any(char.islower() for char in s))
    print(any(char.isupper() for char in s))

# Text Alignment

# Enter your code here. Read input from STDIN. Print output to STDOUT
thick = int(input())
filler = "H"

for i in range(thick): # to create the top arrow, by increasing the width
    print((filler*i).rjust(thick-1) + filler + (filler*i).ljust(thick-1))
for i in range(thick+1): #to create the top column
    print((filler*thick).center(thick*2) + (filler*thick).center(thick*6))
for i in range((thick+1)//2): # to create the middle, by printing as 5 times the thickness
    print((filler*thick*5).center(thick*6))
for i in range(thick+1): #to create the bottom column, as the top column
    print((filler*thick).center(thick*2)+(filler*thick).center(thick*6))
for i in range(thick): #to create the bottom arrow, by decreasing the width
    print(((filler*(thick-i-1)).rjust(thick)+filler+(filler*(thick-i-1)).ljust(thick)).rjust(thick*6))

# Text Wrap

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

# Designer Door Mat

# Enter your code here. Read input from STDIN. Print output to STDOUT
def door_mat_design(n, m):
    # Upper part of the mat
    for i in range(n // 2):
        pattern = '.|.' * (2 * i + 1)
        print(pattern.center(m, '-'))

    # Middle part of the mat
    print('WELCOME'.center(m, '-'))

    # Lower part of the mat
    for i in range(n // 2 - 1, -1, -1):
        pattern = '.|.' * (2 * i + 1)
        print(pattern.center(m, '-'))

if __name__ == '__main__':
    n, m = map(int, input().split())
    door_mat_design(n, m)

# String Formatting

def print_formatted(number):
    # your code goes here
    width = len(bin(number)) - 2
    for i in range(1, number + 1):
        decimal = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]
        print(decimal.rjust(width), octal.rjust(width), hexadecimal.rjust(width), binary.rjust(width))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

# Alphabet Rangoli

def make_line(number_of_letters, size):
    x = 97 + size - number_of_letters
    line = ""
    for i in range(number_of_letters -1, -1, -1):
        line += chr(x+i) + "-"
    for i in range(1, number_of_letters):
        line += chr(x+i) + "-"
    return line[:-1]

def print_rangoli(size):
    m= ((size*2)-1) + (size-1) * 2
    for i in range(1, size+1):
        pattern = make_line(i, size)
        print(pattern.center(m, "-"))
    for j in range(size -1, 0, -1):
        pattern2 = make_line(j, size)
        print(pattern2.center(m, "-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

# Capitalize!

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    return " ".join([fullname.capitalize() for fullname in s.split(" ")])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

# The Minion Game

def minion_game(string):
    # your code goes here
    kevin_score = 0
    stuart_score = 0
    length = len(string)

    for i in range(length):
        if string[i] in 'AEIOU':
            kevin_score += length - i
        else:
            stuart_score += length - i

    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)

# Merge the Tools!

def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        substring = string[i:i + k]
        seen = set()
        unique_substring = ''.join([char for char in substring if not (char in seen or seen.add(char))])
        print(unique_substring)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

# Introduction to Sets

def average(array):
    # your code goes here
    return round(sum(set(array)) / len(set(array)), 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

# Symmetric Difference

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    m = int(input())
    a = set(map(int, input().split()))
    n = int(input())
    b = set(map(int, input().split()))

    symmetric_diff = a.symmetric_difference(b)

    for num in sorted(symmetric_diff):
        print(num)

# No Idea!

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    like = set(map(int, input().split()))
    dislike = set(map(int, input().split()))

    happiness = 0

    for number in arr:
        if number in like:
            happiness += 1
        elif number in dislike:
            happiness -= 1

    print(happiness)

# Set .add()

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())
    stamps = set()

    for _ in range(n):
        country = input().strip()
        stamps.add(country)

    print(len(stamps))

# Set .discard(), .remove() & .pop()

n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    commands = input().split()
    if commands[0] == "pop":
        s.pop()
    elif commands[0] == "remove":
        s.remove(int(commands[1]))
    else:
        s.discard(int(commands[1]))
print(sum(s))

# Set .union() Operation

n = int(input())
english_subscribers = set(map(int, input().split()))
m = int(input())
french_subscribers = set(map(int, input().split()))
total_subscribers = english_subscribers.union(french_subscribers)
print(len(total_subscribers))

# Set .intersection() Operation

n = int(input())
english_subscribers = set(map(int, input().split()))
m = int(input())
french_subscribers = set(map(int, input().split()))
common_subscribers = english_subscribers.intersection(french_subscribers)
print(len(common_subscribers))

# Set .difference() Operation

n = int(input())
english_subscribers = set(map(int, input().split()))
m = int(input())
french_subscribers = set(map(int, input().split()))
only_english = english_subscribers.difference(french_subscribers)
print(len(only_english))

# Set .symmetric_difference() Operation

n = int(input())
english_subscribers = set(map(int, input().split()))
m = int(input())
french_subscribers = set(map(int, input().split()))
result = english_subscribers.symmetric_difference(french_subscribers)
print(len(result))

# Set Mutations

n = int(input())
s = set(map(int, input().split()))
m = int(input())

for _ in range(m):
    operation, _ = input().split()
    other_set = set(map(int, input().split()))

    if operation == "update":
        s.update(other_set)
    elif operation == "intersection_update":
        s.intersection_update(other_set)
    elif operation == "difference_update":
        s.difference_update(other_set)
    elif operation == "symmetric_difference_update":
        s.symmetric_difference_update(other_set)

print(sum(s))

# The Captain's Room

from collections import Counter

k = int(input())
room_numbers = list(map(int, input().split()))

room_count = Counter(room_numbers)

for room, count in room_count.items():
    if count == 1:
        print(room)
        break

# Check Subset

t = int(input())
for _ in range(t):
    input()
    set_a = set(map(int, input().split()))
    input()
    set_b = set(map(int, input().split()))
    print(set_a.issubset(set_b))

# Check Strict Superset

set_a = set(input().split())
n = int(input())
is_strict_superset = True

for _ in range(n):
    set_b = set(input().split())
    if not (set_a > set_b):
        is_strict_superset = False
        break

print(is_strict_superset)

# collections.Counter()

from collections import Counter

n = int(input())
shoe_sizes = list(map(int, input().split()))
shoe_inventory = Counter(shoe_sizes)

total_earnings = 0
m = int(input())

for _ in range(m):
    size, price = map(int, input().split())
    if shoe_inventory[size] > 0:
        total_earnings += price
        shoe_inventory[size] -= 1

print(total_earnings)

# DefaultDict Tutorial

from collections import defaultdict

n, m = map(int, input().split())
group_a = [input().strip() for _ in range(n)]
group_b = [input().strip() for _ in range(m)]

positions = defaultdict(list)

for index, word in enumerate(group_a):
    positions[word].append(index + 1)

for word in group_b:
    if word in positions:
        print(" ".join(map(str, positions[word])))
    else:
        print(-1)

# Collections.namedtuple()

from collections import namedtuple
n = int(input())
columns = input().split()
Student = namedtuple('Student', columns)
print(f"{sum(int(Student(*input().split()).MARKS) for _ in range(n)) / n:.2f}")

# Collections.OrderedDict()

from collections import OrderedDict

n = int(input())
ordered_dict = OrderedDict()

for _ in range(n):
    item, price = input().rsplit(' ', 1)
    price = int(price)
    ordered_dict[item] = ordered_dict.get(item, 0) + price

for item, net_price in ordered_dict.items():
    print(item, net_price)

# Word Order

from collections import OrderedDict

n = int(input())
word_count = OrderedDict()

for _ in range(n):
    word = input().strip()
    word_count[word] = word_count.get(word, 0) + 1

print(len(word_count))
print(' '.join(map(str, word_count.values())))

# Collections.deque()

from collections import deque

d = deque()
n = int(input())

for _ in range(n):
    operation = input().strip().split()
    command = operation[0]

    if command == 'append':
        d.append(operation[1])
    elif command == 'appendleft':
        d.appendleft(operation[1])
    elif command == 'pop':
        d.pop()
    elif command == 'popleft':
        d.popleft()

print(' '.join(d))

# Piling Up!

for _ in range(int(input())):
    n = int(input())
    cubes = list(map(int, input().split()))

    left, right = 0, n - 1
    last_picked = float('inf')
    possible = True

    while left <= right:
        if cubes[left] >= cubes[right]:
            current = cubes[left]
            left += 1
        else:
            current = cubes[right]
            right -= 1

        if current > last_picked:
            possible = False
            break

        last_picked = current

    print("Yes" if possible else "No")

# Company Logo

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    counter = Counter(s)
    most_common = sorted(counter.items(), key=lambda x: (-x[1], x[0]))

for char, count in most_common[:3]:
    print(char, count)

# Calendar Module

import calendar

date_input = input()
month, day, year = map(int, date_input.split())
day_of_week = calendar.weekday(year, month, day)
days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
print(days[day_of_week])

# Time Delta

#!/bin/python3

import math
import os
import random
import re
import sys

from datetime import datetime

def time_delta(t1, t2):
    format_str = '%a %d %b %Y %H:%M:%S %z'

    time1 = datetime.strptime(t1, format_str)
    time2 = datetime.strptime(t2, format_str)

    delta = abs(int((time1 - time2).total_seconds()))

    return delta

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(str(delta) + '\n')

    fptr.close()

# Exceptions

t = int(input())

for _ in range(t):
    a, b = input().split()

    try:
        result = int(a) // int(b)
        print(result)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)

# Zipped!

n, x = map(int, input().split())
marks = [list(map(float, input().split())) for _ in range(x)]

for student_marks in zip(*marks):
    print(sum(student_marks) / x)

# Athlete Sort

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    arr.sort(key=lambda x: x[k])

    for row in arr:
        print(*row)

# ginortS

s = input()
sorted_s = sorted(s, key=lambda x: (x.isdigit() and int(x) % 2 == 0, x.isdigit(), x.isupper(), x.islower(), x))
print(''.join(sorted_s))

# Map and Lambda Function

cube = lambda x: x**3 # complete the lambda function

def fibonacci(n):
    # return a list of fibonacci numbers
    fib_list = [0, 1]
    for i in range(2, n):
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list[:n]



if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

# Detect Floating Point Number

t = int(input())

for _ in range(t):
    s = input()
    try:
        float(s)
        if s.count('.') == 1:
            print(True)
        else:
            print(False)
    except ValueError:
        print(False)

# Re.split()

regex_pattern = r"[,.]"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))

# Group(), Groups() & Groupdict()

import re

s = input()
match = re.search(r'([a-zA-Z0-9])\1+', s)

if match:
    print(match.group(1))
else:
    print(-1)

# Re.findall() & Re.finditer()
import re
s=input()
pattern=r'([^aeiouAEIOU|\s|\+|\-]{1,})([aeiouAEIOU]{2,})([^aeiouAEIOU|\s|\+|\-]{1,}).*'
pattern2='([aeiouAEIOU]{2,})'
findall=re.findall(pattern,s)
if not findall:
    print("-1")
else:
    while findall:
        finditer=re.finditer(pattern,s)

        for i in finditer:
            print(i.groups()[1])
            x=re.search(pattern2,s)
            s=s[x.end():]
            findall=re.findall(pattern,s)

# Re.start() & Re.end()

import re

s = input()
sub_s = input()
pattern = re.compile(f'(?=({sub_s}))')

matches = pattern.finditer(s)
result = [(m.start(1), m.start(1) + len(sub_s) - 1) for m in matches]

if result:
    for r in result:
        print(r)
else:
    print((-1, -1))

# Regex Substitution

import re

n = int(input())
for _ in range(n):
    line = input()
    line = re.sub(r'(?<= )&&(?= )', 'and', line)
    line = re.sub(r'(?<= )\|\|(?= )', 'or', line)
    print(line)

# Validating Roman Numerals

regex_pattern = r"^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))

# Validating phone numbers

import re

n = int(input())
for _ in range(n):
    number = input().strip()
    regex_pattern = r'^[789]\d{9}$'
    print("YES" if re.match(regex_pattern, number) else "NO")

# Validating and Parsing Email Addresses

import email.utils
import re

n = int(input())
rx = re.compile(r"^[a-zA-Z][\w\.\-_]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$")
emails = [email.utils.parseaddr(input()) for _ in range(n)]
emails = filter(lambda x: rx.match(x[1]), emails)
print(*list(map(email.utils.formataddr, emails)), sep='\n')

# Hex Color Code

import re

pattern = r"(#[0-9a-fA-F]{3}|#[0-9a-fA-F]{6})(?=[;),])"
n = int(input())
print(*[i for l in [re.findall(pattern, input()) for _ in range(n)] for i in l], sep="\n")

# HTML Parser - Part 1

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1] if attr[1] is not None else 'None'}")

    def handle_endtag(self, tag):
        print(f"End   : {tag}")

    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1] if attr[1] is not None else 'None'}")

n = int(input())
html_code = ""
for _ in range(n):
    html_code += input()

parser = MyHTMLParser()
parser.feed(html_code)

# HTML Parser - Part 2

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment")
            print(data)
        else:
            print(">>> Single-line Comment")
            print(data)

    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)









html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()

# Detect HTML Tags, Attributes and Attribute Values

# Enter your code here. Read input from STDIN. Print output to STDOUT

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")

    def handle_endtag(self, tag):
        pass

    def handle_startendtag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")

html = ""
for _ in range(int(input())):
    html += input().rstrip() + '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()

# Validating UID

for i in range(int(input())):
    string = list(input())
    a = len(string)

    b = len(list(set(string)))

    result01 = ''
    result02 = ''
    result03 = ''
    result04 = ''
    result05 = ''
    count01 = 0
    count02 = 0

    if(a == 10):
        result05 = True
        if(a == b):
            result04 = True
            for item in string:
                if(65<=ord(item)<=90):
                    count01 = count01 + 1

                if(48<=ord(item)<=57):
                    count02 = count02 +1

                if((97<=ord(item)<=122) or (65<=ord(item)<=90) or (48<=ord(item)<=57)):
                    result03 = True
                else:
                    result03 = False
                    break
        else:
            result04 = False
    else:
        result05 = False



    if(count01 >=2):
        result01 = True
    else:
        result01 = False

    if(count02>=3):
        result02 = True
    else:
        result02 = False

    if((result01 == True) and (result02 == True) and (result03 == True) and (result04 == True) and (result05 == True)):
        print('Valid')
    else:
        print('Invalid')

# Validating Credit Card Numbers

import re

def check_cb(cnum):
    if not bool(re.match(r"^[4,5,6]",cnum)):return "Invalid"
    if not bool(re.match(r"^\d{4}-\d{4}-\d{4}-\d{4}$|^\d{4}\d{4}\d{4}\d{4}$",cnum)):return "Invalid"
    if bool(re.search(r'(.)\1{3}',re.sub(r'\D', '', cnum))):return "Invalid"
    return "Valid"
n = int(input())
print("\n".join([check_cb(input()) for _ in range(n)]))

# Validating Postal Codes

regex_integer_in_range = r"^(0|[1-9]\d{0,5}|100000)$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(?=(\d)(?=\d\1))"	# Do not delete 'r'.


import re
P = input()

print (bool(re.match(regex_integer_in_range, P))
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

# Matrix Script

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)


decoded_script = ''.join(matrix[i][j] for j in range(m) for i in range(n))
result = re.sub(r'(?<=\w)([^\w]+)(?=\w)', ' ', decoded_script)

print(result)

# XML 1 - Find the Score

import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    score = 0
    for elem in node.iter():
        score += len(elem.attrib)
    return score

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))

# XML2 - Find the Maximum Depth

import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    level += 1
    maxdepth = max(maxdepth, level)
    for child in elem:
        depth(child, level)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)

# Standardize Mobile Number Using Decorators

from re import sub

def wrapper(f):
    r = r"^(?:\+?91|0)??(\d{5})(\d{5})$"
    s = r"+91 \1 \2"

    def fun(li):
        return f([sub(r, s, i) for i in li])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)

# Decorators 2 - Name Directory

import operator

def person_lister(f):
    def inner(people):
        # complete the function
        sorted_people = sorted(people, key=lambda x: int(x[2]))
        return [f(person) for person in sorted_people]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

# Arrays

import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    return numpy.array(arr, float)[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

# Shape and Reshape

import numpy

arr = list(map(int, input().strip().split()))
result = numpy.reshape(arr, (3, 3))
print(result)

# Transpose and Flatten

import numpy

n, m = map(int, input().strip().split())
matrix = [list(map(int, input().strip().split())) for _ in range(n)]
array = numpy.array(matrix)
print(numpy.transpose(array))
print(array.flatten())

# Concatenate

import numpy

n, m, _ = map(int, input().split())
a1 = numpy.vstack([list(map(int, input().split())) for _ in range(n)])
a2 = numpy.vstack([list(map(int, input().split())) for _ in range(m)])
print(numpy.concatenate((a1, a2), axis=0))

# Zeros and Ones

import numpy as np

x = tuple(map(int, input().split()))

zer= np.zeros(x, int)

un = np.ones(x, int)

print(zer)

print(un)

# Eye and Identity

import numpy as np

np.set_printoptions(legacy='1.13')

N, M = map(int, input().split())

print(np.eye(N, M))

# Array Mathematics

import numpy

n, m = map(int, input().strip().split())
a = numpy.array([list(map(int, input().strip().split())) for _ in range(n)])
b = numpy.array([list(map(int, input().strip().split())) for _ in range(n)])

print(a + b)
print(a - b)
print(a * b)
print(numpy.floor_divide(a, b))
print(a % b)
print(numpy.power(a, b))

# Floor, Ceil and Rint

import numpy as np
np.set_printoptions(legacy='1.13')
A = np.array(tuple(map(float,input().split())))
print("%s\n%s\n%s"%(np.floor(A),np.ceil(A),np.rint(A)))

# Sum and Prod

import numpy

n, m = map(int, input().strip().split())
array = numpy.array([list(map(int, input().strip().split())) for _ in range(n)])
result = numpy.prod(numpy.sum(array, axis=0))
print(result)

# Min and Max

import numpy

n, m = map(int, input().strip().split())
array = numpy.array([list(map(int, input().strip().split())) for _ in range(n)])
result = numpy.max(numpy.min(array, axis=1))
print(result)

# Mean, Var, and Std

import numpy as np
N,M = map(int,input().split())
Na =np.array([list(map(int,input().split())) for _ in range(N)])
print(f"{np.mean(Na,axis=1)}\n{np.var(Na,axis=0)}\n{round(np.std(Na),11)}")

# Dot and Cross

import numpy

n = int(input())
A = numpy.array([list(map(int, input().strip().split())) for _ in range(n)])
B = numpy.array([list(map(int, input().strip().split())) for _ in range(n)])
print(numpy.matmul(A, B))

# Inner and Outer

import numpy

A = numpy.array(list(map(int, input().strip().split())))
B = numpy.array(list(map(int, input().strip().split())))

print(numpy.inner(A, B))
print(numpy.outer(A, B))

# Polynomials

import numpy

coefficients = list(map(float, input().strip().split()))
x_value = float(input().strip())

result = numpy.polyval(coefficients, x_value)

print(result)

# Linear Algebra

import numpy

n = int(input().strip())
matrix = []

for _ in range(n):
    row = list(map(float, input().strip().split()))
    matrix.append(row)

determinant = numpy.linalg.det(matrix)
print(round(determinant, 2))

# Birthday Cake Candles

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

# Number Line Jumps

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

# Viral Advertising

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

# Recursive Digit Sum

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

# Insertion Sort - Part 1

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

# Insertion Sort - Part 2

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)