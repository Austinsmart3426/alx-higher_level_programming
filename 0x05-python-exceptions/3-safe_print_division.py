#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except (FloatingPointError, ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))

    return result
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy

