class User:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.alias = kwargs.get("alias")

    def display_info(self):
        # convert object to dictionary using __dict__ method and print
        print(self.__dict__)
        # obtain variables object using get 
        print("Name:", self.name)
        print("Alias:", self.alias)