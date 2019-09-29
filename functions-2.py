# using *args to obtain positional arguments
# using **kwargs to obtain key-word arguments in form of a dict

def print_details(*args, **kwargs):
    print(args)
    print(kwargs)

details = {
    "name": "Chris",
    "age": 25
}

print_details(details, color = "Blue", marks = 90, msg="I've always loved this shirt")

