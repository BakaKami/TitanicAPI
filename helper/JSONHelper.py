import json


class JSONHelper:
    @staticmethod
    def to_json(deserialized: any) -> str:
        return json.dumps(deserialized, default=lambda obj: obj.__dict__)

    @staticmethod
    def read_json_from_file(file_name: str) -> any:
        try:
            f = open(f"./encoded/{file_name}.json")
            data = json.load(f)
            f.close()
            return data
        except Exception as error:
            raise Exception("File not found!")
