# -*- coding: utf-8 -*-
"""HW1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Pi_kVxwZ9jf-zBYpuelKXMJe6dGKkbqW
"""

list_odds = [1,3,5,7,9]
list_evens = [0,2,4,6,8]
print(list_odds)
print(list_evens)

new_list = list(list_odds) + list(list_evens)
print(new_list)

new_list_multiplied = [sayı*2 for sayı in new_list]
print(new_list_multiplied)

new_list_multiplied = [2, 6, 10, 14, 18, 0, 4, 8, 12, 16]
for sayı in new_list_multiplied:
  print(type(sayı))