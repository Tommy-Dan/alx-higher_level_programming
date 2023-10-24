#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        diff = a / b
    except (TypeError, ZeroDivisionError):
        diff = None
    finally:
        print("Inside result: {}".format(diff))
    return (diff)
