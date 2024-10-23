import io
from pprint import pprint

def custom_write(file_name, strings):
    strings_positions = {}
    file =open(file_name, 'w', encoding='utf-8')
    pos_ = []
    text_= []
    namber_str = 0
    for i in strings:
        namber_str +=1
        pos_.append((namber_str, file.tell()))
        text_.append(i)
        file.write(f'{i}\n')
    file.close()
    strings_positions = dict(zip(pos_, text_))
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

