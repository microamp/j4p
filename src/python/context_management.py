def main():
    with open("sample.txt") as f:
        for line in f:
            print("line: %s" % line)


if __name__ == "__main__":
    main()
