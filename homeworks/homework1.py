class Home:

    def new(self, arg: int):
        try:
            arg = int(arg)
            return True
        except ValueError:
            return 'ValueError'


home1 = Home()
print(home1.new(4))
print(home1.new('d'))
