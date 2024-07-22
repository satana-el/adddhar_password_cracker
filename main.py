import argparse
import PyPDF2
import sys


def main():
    parser = argparse.ArgumentParser("PDF password cracker")
    parser.add_argument("-f", help="Path of the file to crack")
    parser.add_argument("-p", help="password file")
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_usage()
        sys.exit(1)

    passwords = list(readpass(args.p))
    print(crack(args.f, passwords))

    sys.exit(0)


def readpass(filename):
    with open(filename) as file:
        for line in file:
            yield line.rstrip()


def crack(filename, passwords):
    with open(filename, "rb") as file:
        reader = PyPDF2.PdfReader(file)

        if reader.is_encrypted:
            for password in sorted(passwords):
                try:
                    if reader.decrypt(password):
                        return f"Successfully decrypted with password: {password}"
                except Exception as e:
                    pass
            else:
                return f"File isn't password protected."


if __name__ == "__main__":
    main()
