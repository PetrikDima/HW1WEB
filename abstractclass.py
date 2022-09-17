import json
import pickle


class SerializationInterface:
    def __init__(self, value):
        self.value = value

    def serialize_file(self, format, file_name, action):
        with open(file_name, action) as file:
            format.dump(self.value, file)


class JsonFormat(SerializationInterface):
    def __init__(self, value):
        super(JsonFormat, self).__init__(value)

    def serialize_file(self, *args):
        return super().serialize_file(json, 'data.json', 'w')


class BinFormat(SerializationInterface):
    def __init__(self, value):
        super(BinFormat, self).__init__(value)

    def serialize_file(self, *args):
        return super().serialize_file(pickle, 'data.bin', 'wb')

