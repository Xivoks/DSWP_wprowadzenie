
x, y = input("Enter two values (separated by a comma) : ").split(",")
print("First variable: ", x)
print("Second variable: ", y)
print("\n")

sourceSeparator = input("Enter source separator : ")
destinationSeparator = input("Enter destination separator : ")
text = input("Enter text for separate: ").split(sourceSeparator)

textDestination=destinationSeparator.join(text);
print(textDestination)
