import base64

def encrypt():
	plain = raw_input('Enter the plaintext message: ')
	keyCaesar = int(raw_input('Enter the secret key: '))
	temp1 = ''

	for i in plain:
		temp1 += chr(ord(i)+keyCaesar)

	temp2 = base64.b64encode(temp1)
	temp3 = ''

	for i in temp2:
		temp3 += chr(ord(i)+keyCaesar)

	temp4 = base64.b32encode(temp3)
	temp5 = ''

	for i in temp4:
		temp5 += chr(ord(i)+keyCaesar)
	
	chiper = temp5
	
	print 'Ciphertext: {}\n'.format(chiper)
	input("Press enter to close program")

def decrypt():
	chiper = raw_input('Enter the chipertext message: ')
	key = int(raw_input('Enter the secret key: '))

	temp1 = ''

	for i in chiper:
		temp1 += chr(ord(i)-key)

	temp2 = base64.b32decode(temp1)
	temp3 = ''

	for i in temp2:
		temp3 += chr(ord(i)-key)

	temp4 = base64.b64decode(temp3)

	temp5 = ''

	for i in temp4:
		temp5 += chr(ord(i)-key)

	plain = temp5

	print 'Plaintext: {}\n'.format(plain)
	input("Press enter to close program")

choice=int(raw_input("Please press 1 for encryption or 2 for decryption: "));
if choice==1:
	encrypt();
elif choice==2:
	decrypt();
else:
	print("Wrong choice entered. Exiting now..");
	exit();
