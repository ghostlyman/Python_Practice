class A:
    __class_private_var = 'class private var' #定义了两个类变量
    class_public_var = 'class public var'

    def __init__(self):
        self.__instance_private_var = 'instance private var'  #定义的两个实例变量
        self.__instance_public_var = 'instance public var'

    def __instance_private_method(self):  # 实例方法
        try:
            print(self.__class_private_var)
        except:
            pass
        try:
            print(self.class_public_var)
        except:
            pass
        try:
            print(self.__instance_private_var)
        except:
            pass
        try:
            print(self.__instance_public_var)
        except:
            pass

    def instance_public_method(self):
        try:
            print(self.__class_private_var)
        except:
            pass
        try:
            print(self.class_public_var)
        except:
            pass
        try:
            print(self.__instance_private_var)
        except:
            pass
        try:
            print(self.__instance_public_var)
        except:
            pass

    @classmethod
    def __private_class_method(cls):
        try:
            print(cls.__class_private_var)
        except:
            pass
        try:
            print(cls.class_public_var)
        except:
            pass

    @classmethod
    def public_class_method(cls):
        try:
            print(cls.__class_private_var)
        except:
            pass
        try:
            print(cls.class_public_var)
        except:
            pass


class B(A):
    pass

b = B() #初始化实例

print(dir(B))


b.__instance_private_method()   #error
b.__private_class_method()   #error
b.instance_public_method()  # display four var
b.public_class_method()   #display two var

#私有的方法, 变量(类和实例)是不可继承的
#公有的方法, 变量(类和实例)是可继承的
#父类公有的方法(类和实例)是可以访问父类的私有变量的


class B(A):
    __class_private_var = 'Childs class private var'
    class_public_var = 'Childs class public var'

    def __init__(self):
        super(B, self).__init__()
        self.__instance_private_var = 'child instance private var'
        self.instance_public_var = 'child instance public var'

b = B()

b.instance_public_method()



