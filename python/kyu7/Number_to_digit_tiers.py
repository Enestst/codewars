def create_array_of_tiers(n):
	list = []
	for i in range(1,len(str(n)) + 1):
		list.append(str(n)[0:i])
	return list


print(create_array_of_tiers(0))