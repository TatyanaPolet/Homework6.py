my_dict = {'Andrey': 1999, 'Stas': 1990, 'Kirill': 2020}  # This is a sample Python script.
print ('Dict: ', my_dict)
print ('Existing value: ', my_dict ['Kirill'])
print ('Not existing value: ', my_dict.get ('Venya'))
my_dict.update({'Sveta': 2000,
                'Katya': 2017})
my_dict.pop ('Andrey')
my_dict = {'Andrey': 1999, 'Stas': 1990, 'Kirill': 2020}  # This is a sample Python script.
my_dict.update({'Sveta': 2000,
              'Katya': 2017})
a = my_dict.pop ('Andrey')
print ('Deleted value: ', a)
print ('Modified dictionery: ', my_dict)
my_set = {5,23, 6.6, 5, 5, 'fond', 'fond', False, (6,24,5.3)}
print ('Set: ', my_set)
print (my_set.add(8))
print ('Modified set: ', my_set)
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
