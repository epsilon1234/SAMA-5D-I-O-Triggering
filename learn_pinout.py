from mpio import GPIO

def main():
    for i in range (127):
        pin = GPIO.pin_to_name(i)
        number=GPIO._pin_lookup(i)
        print(pin, number)


if __name__ == "__main__":
    main()
