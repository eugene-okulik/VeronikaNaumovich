response_1 = "результат операции: 42"
number_1 = int(response_1[response_1.index(':') + 2:])
print(number_1 + 10)

response_2 = "результат операции: 514"
number_2 = int(response_2[response_2.index(':') + 2:])
print(number_2 + 10)

response_3 = "результат работы программы: 9"
number_3 = int(response_3[response_3.index(':') + 2:])
print(number_3 + 10)
