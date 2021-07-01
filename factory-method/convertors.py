class StrConvertor:
    def convert(value) -> str:
        return str(value)


class FloatConvertor:
    def convert(value) -> float:
        return float(value)


class ConvertorFactory:
    def __init__(self):
        self.convertors = {}

    def register_convertor(self, new_type, convertor):
        self.convertors[new_type] = convertor

    def get_convertor(self, desired_type):
        if desired_type not in self.convertors:
            raise ValueError(desired_type)
        return self.convertors[desired_type]


factory = ConvertorFactory()
factory.register_convertor("str", StrConvertor)
factory.register_convertor("float", FloatConvertor)
