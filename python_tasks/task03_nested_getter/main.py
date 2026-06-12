def get_by_path(data, path: str):
    current = data
    for part in path.split("."):
        if isinstance(current, dict):
            current = current[part]
        else:
            current = current[int(part)]
    return current


if __name__ == "__main__":
    nested = {"a": {"b": {"c": "+++"}}}
    print(get_by_path(nested, "a.b.c"))
