# $player = new Http('https://en-gb.facebook.com/{username}/', array(
# 	'username' => $uname,
# ));
class Person:
    def __init__(self,name : str, work: list ,city : str='Roorkee') :
        self.name = name
        self.city = city
        self.work = work

    def show(self) :
        print(self.name)
        print(self.city)
        print(self.work)

p = Person("sweety")
p.show()