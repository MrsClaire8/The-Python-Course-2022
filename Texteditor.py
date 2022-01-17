typing = []

while True:
    text = input('Type something: ')
    if text != 'exit':
        typing.append(text)
    else:
        break


for tekst in typing:
    tekst.title()
#print ('. '.join(text.title() for text in typing)+'.')
print('. '.join(typing))