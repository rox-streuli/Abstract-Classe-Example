# To start with ABC you should:
#
# import the abc module;
# make your base class inherit the helper class ABC, which is
# delivered by the abc module;
# decorate abstract methods with @abstractmethod, which is
# delivered by the abc module.
# When you run the code, the output doesn’t surprise anyone:
#
import abc


class BluePrint(abc.ABC):
    @abc.abstractmethod
    def hello(self):
        pass


class GreenField(BluePrint):
    def hello(self):
        print('Welcome to Green Field!')


gf = GreenField()
gf.hello()

# Outputs...
# Welcome to Green Field!

# You can not instantiate the BluePrint class!!!!
# bp = BluePrint()

# Will output...
# Traceback (most recent call last):
#   File "C:/Users/R G Streuli/PycharmProjects/Cisco_PCPP/abstract_classe1.py",
#   line 78, in <module>
#     bp = BluePrint()
# TypeError: Can't instantiate abstract class BluePrint with abstract methods
# hello

# When the base class provides one or more abstract methods,
# all of them must be overridden in a subclass before the subclass
# can be instantiated.
