def decimal_to_binary (decimal):
	# your code here
	binary_number = ''
	while decimal >= 2:
		binary_number += str(decimal % 2)
		decimal = decimal // 2
	binary_number += str(decimal)
	return binary_number[::-1]

print(decimal_to_binary(3))
print(decimal_to_binary(8))
print(decimal_to_binary(15))
print(decimal_to_binary(16))
