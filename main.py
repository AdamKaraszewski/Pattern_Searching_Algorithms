import random
import string

import matplotlib.pyplot as plt

from naive_pattern_search import naive_pattern_search as naive
from sunday_pattern_search import sunday_pattern_search as sunday
from generate_string import generate_string as generator

# O(T)
alphabet= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

pattern_t = generator(alphabet, 5)
x_axis_t = range(5, 9996)
y_axis_naive_t = []
y_axis_sunday_t = []
text_t = generator(alphabet, 5)
for i in x_axis_t:
    y_axis_naive_t.append(naive(pattern_t, text_t)[1])
    y_axis_sunday_t.append(sunday(alphabet, pattern_t, text_t)[1])
    # y_axis_mp_t.append(mp(pattern_t, text_t)[1])
    text_t += random.choice(alphabet)

# O(P)
text_p = generator(alphabet, 10000)
x_axis_p = range(41)
y_axis_naive_p = []
y_axis_sunday_p = []
pattern_p = 'a'
for i in x_axis_p:
    y_axis_naive_p.append(naive(pattern_p, text_p)[1])
    y_axis_sunday_p.append(sunday(alphabet, pattern_p, text_p)[1])
    pattern_p += random.choice(alphabet)

# O(A)
ascii_alphabet = list(string.ascii_lowercase)
x_axis_a = range(1, 11)
y_axis_naive_a = []
y_axis_sunday_a = []
for i in x_axis_a:
    alphabet_a = ascii_alphabet[:i]
    pattern_a = generator(alphabet_a, 10)
    text_a = generator(alphabet_a, 1000)
    y_axis_naive_a.append(naive(pattern_a, text_a)[1])
    y_axis_sunday_a.append(sunday(alphabet_a, pattern_a, text_a)[1])

plt.figure()
plt.xlabel('text size')
plt.ylabel('complexity')
plt.title('O(text_size)')
plt.grid()
plt.plot(x_axis_t, y_axis_naive_t, label='Naive Pattern Search O(T)')
plt.plot(x_axis_t, y_axis_sunday_t, label='Sunday Pattern Search O(T)')
plt.legend()

plt.figure()
plt.xlabel('pattern size')
plt.ylabel('complexity')
plt.title('O(pattern_size)')
plt.grid()
plt.plot(x_axis_p, y_axis_naive_p, label='Naive Pattern Search O(P)')
plt.plot(x_axis_p, y_axis_sunday_p, label='Sunday Pattern Search O(P)')
plt.legend()

plt.figure()
plt.xlabel('alphabet size')
plt.ylabel('complexity')
plt.title('O(alphabet_size)')
plt.grid()
plt.plot(x_axis_a, y_axis_naive_a, label='Naive Pattern Search O(A)')
plt.plot(x_axis_a, y_axis_sunday_a, label='Sunday Pattern Search O(A)')
plt.legend()

plt.show()