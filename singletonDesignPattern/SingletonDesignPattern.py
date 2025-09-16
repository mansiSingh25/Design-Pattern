class Singleton:
    # Create a private class-level variable to hold the single instance
    __unique_instance = None

    #  Make the constructor "private-like"
    # In Python, we can't make it truly private, but we can prevent direct use by controlling instantiation
    def __init__(self):
        if Singleton.__unique_instance is not None:
            raise Exception("This class is a singleton! Use get_instance() instead.")

    #  Create a  get_instance class method to get the single instance
    @classmethod
    def get_instance(cls):
        if cls.__unique_instance is None:
            cls.__unique_instance = Singleton()
        return cls.__unique_instance
