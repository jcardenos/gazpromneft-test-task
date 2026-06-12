import json


def parse_json(in_data: str):
    return json.loads(in_data)


if __name__ == "__main__":
    in_data = '{"one": ["http", "yandex.ru"], "two": ["https", "google.com"]}'
    out_data = parse_json(in_data)
    print(out_data)
