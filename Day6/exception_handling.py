if not os.path.exists("abc.txt"):
  with open("abc.txt", 'w') as file:
      file.write("File created")
      print("File created")
else:
  print("file present")

try:
  with open("abc.txt", "r") as file:
    file.write("Experiment")
except FileNotFoundError as fileError:
  print("File is not present, please create the file \"abc.txt\", error as: " + str(fileError))
except io.UnsupportedOperation as error:
  print("Error occurred: " + str(error))