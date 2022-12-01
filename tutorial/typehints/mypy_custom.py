class MyClass:
    def foo(self):
        pass


def get_my_class() -> MyClass:
    return MyClass()


instance = get_my_class()
instance.foo()
instance.unknown()  # error: "MyClass" has no attribute "unknown"
