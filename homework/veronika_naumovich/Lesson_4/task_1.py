my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': ['яблоко', 'банан', 'слива', 'груша', 'апельсин'],
    'dict': {
        'a': 6,
        'b': 7,
        'c': 8,
        'd': 9,
        'e': 10
    },
    'set': {10, 20, 30, 40, 50}
}
print('Последний элемент кортежа:', my_dict['tuple'][-1])

my_dict['list'].append('виноград')
my_dict['list'].pop(1)
print(my_dict['list'])

my_dict['dict'][('i am a tuple',)] = '11'
my_dict['dict'].pop('a')
print(my_dict['dict'])

my_dict['set'].add(60)
my_dict['set'].pop()
print(my_dict['set'])

