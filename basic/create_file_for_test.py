def create_file_for_test(file_name, _str):
	f = open(file_name, "w")
	f.write(_str)
	f.close()