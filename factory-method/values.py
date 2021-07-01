import convertors

class Value:
    def __init__(self, value):
        self.value = value

    def convert(self, desired_type):
        convertor = convertors.factory.get_convertor(desired_type)
        self.value = convertor.convert(self.value)

    def print_type(self):
        print(type(self.value))


if __name__ == "__main__":
    value = Value(123)
    value.print_type()
    value.convert("float")
    value.print_type()
    # Try out wrong type, expected an exception
    value.convert("int")
