# class Pager(object):
#
#     def __init__(self, page, page_size):
#         # 用户当前请求的页码（第一页、第二页...）
#         self.page = page
#         # 每页默认显示10条数据
#         self.page_size = page_size if page_size < 0 else 10
#
#     @property
#     def start(self):
#         val = (self.page - 1) * self.page_size
#         return val
#
#     @property
#     def end(self):
#         val = self.page * self.page_size
#         return val
#
#
# if __name__ == '__main__':
#     '''' ############### 调用 ############### '''
#     pager = Pager(1, 10)
#     print(pager.start)
#     print(pager.end)

# class Goods():
#     def __init__(self, _price):
#         self._price = _price
#
#     @property
#     def price(self):
#         return self.price
#
#
# if __name__ == '__main__':
#     goods = Goods(30)
#     print(goods.price)

# def triangles():
#     result=[1]
#     while True:
#         yield result
#         l=result[:]
#         if l==[1]:
#             result=[1,1]
#         else:
#             result=[1]
#             n=0
#             while n<len(l)-1:
#                 result.append(l[n]+l[n+1])
#             result.append(1)
#
# triangles()


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


def now():
    print('2015-3-25')


if __name__ == '__main__':
    log(now)()
