def arithmetic_arranger(problems, write = False):
	first_line = ""
	second_line = ""
	third_line = ""
	fourth_line = ""
	if (len(problems) > 5):
		return "Error: Too many problems."
	for problem in problems:
		equation = problem.split()
		first = equation[0]
		second = equation[2]
		sign = equation[1]
		place = max(len(first), len(second))+2
		if not first.isdigit() or not second.isdigit():
			return "Error: Numbers must only contain digits."
		if (int(first) > 9999 or int(second) > 9999):
			return "Error: Numbers cannot be more than four digits."
		if sign == "+":
			res = int(first) + int(second)
		if sign == "-":
			res = int(first) - int(second)
		if sign != "+" and sign != "-":
			return "Error: Operator must be '+' or '-'."
		result = str(res)
		if len(first_line) == 0:
			first_line = (place-len(first))*" "+first
		else:
			first_line = first_line + ((4+place-len(first))*" "+ first)	
		if len(second_line) == 0:
			second_line = sign + (place-1-len(second))*" " + second
		else:
			second_line = second_line + 4*" " + sign + (place-1-len(second))*" " + second
		if len(third_line) == 0:
			third_line += place*"-"
		else:
			third_line = third_line + 4*" " + "-"*place
		if len(fourth_line) == 0:
			fourth_line = (place-len(result))*" " + result
		else:
			fourth_line = fourth_line + 4*" " + (place-len(result))*" " + result
	if (write == True):
		return first_line + "\n" + second_line + "\n" + third_line + "\n" + fourth_line
	else:
		return first_line + "\n" + second_line + "\n" + third_line


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "2 - 1"], True))
