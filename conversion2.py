def xor_c(a, b):
	return '0' if(a == b) else '1'
def flip(c):
	return '1' if(c == '0') else '0'
def binarytoGray(binary):
	gray = ""
	gray += binary[0]
	for i in range(1,len(binary)):
		gray += xor_c(binary[i-1],
		binary[i])
	return gray
def graytoBinary(gray):
	binary = ""
	binary += gray[0]
	for i in range(1, len(gray)):
		if (gray[i] == '0'):
			binary += binary[i-1]
		else:
			binary += flip(binary[i-1])
	return binary

binary = "01001"
print("El código gray de ", binary, "es",
binarytoGray(binary))

gray = "01101"
print("El código binario de ", gray, "es",
graytoBinary(gray))