from pwn import *
import string

r = remote("target", port)

letters = string.ascii_letters
letters += string.punctuation
letters += string.digits

flag = "C"
old_num = 346

while flag[-1] != "}":
	for i in letters:
		test = flag + i
		r.sendlineafter(":", test)
		line = r.recvuntil('clock',timeout=10)
		number = line.strip().split()[4]
		
		if int(number)-old_num > 280:
			# Find
			old_num = int(number)
			flag = test
			print("Flag: " + flag)
		print(test + " - " + str(int(number)) + " " + str(old_num))
		
		#r.interactive()
