""" Project # 1
    Dictionary
    Panukova E.
"""
import local as lc

list_1 = []
list_2 = []
dict_1 = {}
dict_2 = {}

with open('input.txt') as file_in:
    lines = file_in.readlines()
    for line in lines:
        line = line[:-1]
        a = line.find(':')
        b = line.find(';')
        if a != -1:
            line1 = line[a + 1:]
            dict_1[line[:a - 1]] = line1.split(',')
            list_1.append(dict_1)
        if b != -1:
            line2 = line[b + 1:]
            dict_2[line[:b - 1]] = set(line2.split(','))
            list_2.append(dict_2)
    dict_actor = list_2[0]
    dict_dop_info = list_1[0]

print(lc.FILM1)
film_one = str(input())
while film_one not in dict_actor:
    print(lc.ERROR_1)
    film_one = str(input())
print(lc.FILM2)
film_two = str(input())
while film_two not in dict_actor:
    print(lc.ERROR_1)

fir_act = dict_actor[film_one]
fir_inf = dict_dop_info[film_one]
sec_act = dict_actor[film_two]
sec_inf = dict_dop_info[film_two]

actors_in = fir_act & sec_act
ne_fir_act = fir_act - (actors_in)
ne_sec_act = sec_act - (actors_in)

reges_1 = dict_dop_info[film_one][:-2]
reyting_1 = dict_dop_info[film_one][-2]
kategory_1 = dict_dop_info[film_one][-1]

reges_2 = dict_dop_info[film_two][:-2]
reyting_2 = dict_dop_info[film_two][-2]
kategory_2 = dict_dop_info[film_two][-1]

kategory = ''
reges = ''

if kategory_2 == kategory_1:
    kategory = kategory_1
if reges_1[0] == reges_2[0]:
    reges = reges_1[0]

if reges != '' and kategory != '':
    print(lc.ACTORS_IN, end='')
    for i in actors_in:
        print(i, end=' ')
    print(' ')
    print(lc.NE_ACT.format(film_one), end='')
    for j in ne_fir_act:
        print(j, end=' ')
    print(' ')
    print(lc.NE_ACT.format(film_two), end='')
    for k in ne_sec_act:
        print(k, end=' ')
    print(' ')
    print(lc.FR_1.format(film_one, reyting_1))
    print(lc.FR_1.format(film_two, reyting_2))
    print(lc.FR_2.format(kategory, reges))

    print(lc.END)

elif reges == '' and kategory != '':
    print(lc.ACTORS_IN, end='')
    for i in actors_in:
        print(i, end=' ')
    print(' ')
    print(lc.NE_ACT.format(film_one), end='')
    for j in ne_fir_act:
        print(j, end=' ')
    print(' ')
    print(lc.NE_ACT.format(film_two), end='')
    for k in ne_sec_act:
        print(k, end=' ')
    print(' ')
    print(lc.GR.format(film_one, reyting_1, reges_1[0]))
    print(lc.GR.format(film_two, reyting_2, reges_2[0]))
    print(lc.KAT.format(kategory))

    print(lc.END)

elif reges != '' and kategory == '':
    print(lc.ACTORS_IN, end='')
    for i in actors_in:
        print(i, end=' ')
    print(' ')
    print(lc.NE_ACT.format(film_one), end='')
    for j in ne_fir_act:
        print(j, end=' ')
    print(' ')
    print(lc.NE_ACT.format(film_two), end='')
    for k in ne_sec_act:
        print(k, end=' ')
    print(' ')
    print(lc.PR_1.format(film_one, reyting_1, kategory_1))
    print(lc.PR_1.format(film_two, reyting_2, kategory_2))
    print(lc.REGES.format(reges))

    print(lc.END)

else:
    print(lc.ACTORS_IN, end='')
    for i in actors_in:
        print(i, end=' ')
    print(' ')
    print(lc.NE_ACT.format(film_one), end='')
    for j in ne_fir_act:
        print(j, end=' ')
    print(' ')
    print(lc.NE_ACT.format(film_two), end='')
    for k in ne_sec_act:
        print(k, end=' ')
    print(' ')
    print(lc.PAS.format(film_one, reyting_1, kategory_1, reges_1[0]))
    print(lc.PAS.format(film_two, reyting_2, kategory_2, reges_1[0]))

    print(lc.END)
