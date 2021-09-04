def elementChecker(list, element):
	if element in list:
		return f"element is there at index {list.index(element)}"
	else:
		return "element is not there"

List1 = [1,2,3,4,5]
print(elementChecker(List1, 2))
