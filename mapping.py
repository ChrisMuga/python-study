# 1
names = [
    "chris",
    "muga",
    "tom",
    "hardy"
]

list(map(lambda x: print(x.upper()), names))

# 2
people = [
    {
        "name": "Chris Muga",
        "age": 23
    },
    {
        "name": "Donna Sonia",
        "age": 21
    },
    {
        "name": "Nicole Andang'o",
        "age": 17
    }
]

list(map(lambda x: print(x.get("name")), people))