import sys, os



def parseInfo(src, out):
	f = open(src)
	lines = f.readlines()
	lines = map(lambda line: line.replace("County Public Schools", ""), lines);
	lines = map(lambda line: line.replace("City Public Schools", ""), lines);
	target = open(out, 'w+')
	target.write("COUNTY,FY17,FY16,FY15\n")
	for line in lines:
		tokens = line.split()
		county_name = "";
		endingNameIndex = 1;
		if (len(tokens) > 7):
			for index in range(1,len(tokens)):
				token = tokens[index]
				if any(char.isdigit() for char in token):
					break;
				else:
					endingNameIndex = endingNameIndex + 1;

			county_name = "";
			for index in range(1, endingNameIndex):
				if (index == endingNameIndex - 1):
					county_name = county_name + tokens[index]
				else:
					county_name = county_name + tokens[index] + str(" ")

			fy15 = tokens[endingNameIndex].replace(",", "")
			fy16 = tokens[endingNameIndex+1].replace(",", "")
			fy17 = tokens[endingNameIndex+3].replace(",", "")
			arr = [county_name, fy17, fy16, fy15]
			out_str = ','.join(arr)
			target.write(out_str + "\n")

		else:
			county_name = tokens[1]
			fy17 = tokens[2].replace(",", "")
			fy16 = tokens[3].replace(",", "")
			fy15 = tokens[5].replace(",", "")

			arr = [county_name, fy17, fy16, fy15]
			out_str = ','.join(arr)
			target.write(out_str + "\n")
		







if __name__ == "__main__":
	if (len(sys.argv) < 3):
		print(STDERR, "No file name provided")
		exit
	parseInfo(sys.argv[1], sys.argv[2])