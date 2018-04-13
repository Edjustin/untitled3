
#def verify(fun):
    #def decorator():
        #print('这个是用户验证')
        #fun()

    #return decorator

#@verify
#def get_money():
    #print('存款')

#get_money()







#def add(num):
    #for i in range(2, num):
        #count = 0
        #if num % i == 0:
            #count += 1
            #if count > 0:
                #print('合数')
                #break
            #else:
                #print('质数')
                #break
#add(15)


def add(num):
    for i in range(2, num):
        count = 0
        if num % i == 0:
            count += 1
            if count > 0:
                print('合数')
                break
            else:
                print('质数')
                break
add(15)


