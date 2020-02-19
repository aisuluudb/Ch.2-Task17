x = 'Kazakhstan'
y = 'Paris'
z = 'Kyrgyzstan'
offices = ('Here is a list:\n {}\n {}\n {}'.format (x,y,z))
print(offices)
choice = (input('Enter x if Kazakhstan, y if Paris and z if Kyrgyzstan'))


if choice = x:
    with open('kz.txt','w') as file:
        file.write ('this is a google office in Kazakhstan')
    print(file)
elif choice == y:
    with open('pr.txt','w') as file1:
        file1.write ('this is a google office in Paris')
    print(file1)
else:
    with open('kg.txt','w') as file2:
        file2.write ('this is a google office in Kyrgyzstan')
    print(file2)
