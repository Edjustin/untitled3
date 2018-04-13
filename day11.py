# 所有商品的数据
shops = []
# 保存用户购买的信息
shop_car = []
def add_shop(name, price, inc):
    shop = {'name': name, 'price': price, 'inc': inc}
    shop.append(shop)

def delete_shop(name):
    #判断商品是否存在
    if shops:
        #遍历所有商品信息,通过key获取值  进行比较
        for shop in shops:
            # 删除商品
            shops.remove(shop)
            break

def show_shop():
    #选择商品的
    print('请选择您要购买的商品编号')
    i = 0
    for shop in shops:
        i += 1
        print(i, shop)

def choose_shop(shop_num):
    #选择商品添加到购物车
    shop = shops[shop_num - 1]
    shop_car.append(shop)

def pay():
    money = 0
    if shop_car:
        for shop in shop_car:
            money += shop.get('price')
    print('商品的总价{}'.format(money))

    #测试代码
if __name__ == '__main__':
    #测试添加商品信息
    add_shop('iphone X', 8000, '装x专用')
    add_shop('meta11', 5000, 'AI手机')
    print(shops)
    # 测试删除商品信息
    # delete_shop('meta10')
    # print(shops)
    # 选择商品添加到购物车
    choose_shop(1)
    choose_shop(2)
    choose_shop(3)
    choose_shop(4)
    print("购物车商品信息:\n{}".format(shop_car))
    # 测试结算功能
    pay()






