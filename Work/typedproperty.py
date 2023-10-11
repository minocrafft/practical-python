def typedproperty(name, typed):
    @property
    def prop(self):
        return getattr(self, f"_{name}")

    @prop.setter
    def prop(self, value):
        if not isinstance(value, typed):
            raise TypeError(f"Expected {typed}")
        setattr(self, f"_{name}", value)

    return prop


String = lambda name: typedproperty(name, str)
Integer = lambda name: typedproperty(name, int)
Float = lambda name: typedproperty(name, float)
