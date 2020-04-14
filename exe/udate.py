import random
import time

city_list = ["beijing", "shanghai", "nanjing", "guangzhou", "anhui", "shenzheng", "yangquan",
             "hunan", "dengta", "fuguo", "heilongjiang"]

country_list = ["china", "english", "japanese", "france", "america", "australia"]             

name_list = 'qwertyuiopasdfghjklzxcvbnm'

user_list = list()


class User(object):
    def __init__(self):
        pass

def user():
    for i in range(150000):
        user = User()
        user.id = str(i)
        user.city = city_list[random.randrange(0, len(city_list))]
        user.age = str(random.randrange(15, 40))
        user.sex = str(random.randrange(0, 1))
        user.country = country_list[random.randrange(0, len(country_list))]
        user.name = ''
        for n in range(random.randrange(5, 10)):
            user.name = user.name + name_list[random.randrange(0, len(name_list))]
    
        user.birthday =  time.strftime("%Y%m%d", time.localtime(random.randrange(593596791, 909129591)))
    
        user_list.append(user)
        
        s = "\t".join([user.id, user.name, user.country, user.birthday])
    
        print s
    

def data():
    for i in range(20000000):
    
        user = user_list[random.randrange(0, len(user_list))]
    
        stamp = time.localtime(random.randrange(1540210218, 1571746218))
        rstamp = time.strftime("%Y%m%d", stamp)
    
        cost = str(random.randrange(0, 100000))
    
        rmax = str(random.randrange(0, 99999))
        rmin = str(random.randrange(0, 99999))
    
        if rmax < rmin:
            rmax, rmin = rmin, rmax
    
        s = "\t".join(
            [user.id, time.strftime("%Y%m%d", stamp), rstamp, user.city, user.age, user.sex, rstamp,
             cost, rmax, rmin])
    
        print(s)
    

if __name__ == "__main__" :
    user()
