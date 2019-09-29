class User:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name")

    def display_info(self):
        # convert object to dictionary using __dict__ method and print
        print(self.__dict__)
        # obtain variables object using get 
        print(self.name)

user = User(name = "Christian Bale")
user.display_info()