def get_first_item(items):
    try:
        return items[0]
    except IndexError as e:
        print("IndexError: %s" % e)
    except KeyError as e:
        print("KeyError: %s" % e)
    except Exception as e:
        print("Error: %s" % e)


def try_except_finally():
    get_first_item([])  # IndexError: list index out of range
    get_first_item({"a": 1, "b": 2})  # KeyError: 0


if __name__ == "__main__":
    try_except_finally()
