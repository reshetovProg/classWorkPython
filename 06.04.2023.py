class Rectangle:
    def __init__(self, width, height):
        self.__width=width
        self.__height=height


    def get_S(self):
        return self.__width*self.__height

    def compare_b(self, fig2):
        return self.get_S()>fig2.get_S()

    def compare_s(self, fig2):
        return self.get_S()<fig2.get_S()

    def __gt__(self,ob2):
        return self.get_S()>ob2.get_S()

    def __truediv__(self, other):
        return self.get_S()/ob2.get_S()

if __name__=="__main__":
    figure1 = Rectangle(12,10)
    figure2 = Rectangle(12,12)
    # print(f'{figure1.get_S()}, {figure2.get_S()}')
    #
    # if figure1.get_S() > figure2.get_S(): print('figure1')
    # if figure1.get_S() < figure2.get_S(): print('figure2')
    # else: print('==')

    # drob1 = Drob(2,3)
    # drob2 = Drob(2, 6)
    # drob3 = drob1/drob2


class Drob:
    def __init__(self,num,denum):
        self.num=num
        self.denum=denum
    def __add__(self, other):
        num=self.num*other.denum+self.denum*other.num
        denum=self.denum*other.denum
        return Drob(num,denum)
    def show(self):
        print(self.num,'/',self.denum)
    def __mul__(self, other):
        return Drob(
            self.num*other.num,
            self.denum*other.denum
        )
if __name__=='__main__':
    d1=Drob(2,5)
    d2=Drob(3,4)
    sum=d1+d2
    sum.show()
    mult=d1*d2
    mult.show()

id_book=1
class Book:
    def __init__(self,name,author,publ):
        global id_book
        self.book={id_book:[name,author,publ]}
        id_book+=1
    def show(self):
        print(self.book)

class Library:
    book_list=[]
    def add(self,book):
        self.book_list.append(book)
    def show_all(self):
        for i in self.book_list:
            i.show()

    def remove(self,book):
        self.book_list.remove(book)

if __name__ == '__main__':
    book1=Book("AAA","BBB","ACT")
    book2 = Book("AAA2", "BBB", "ACT")
    lb=Library()
    lb.add(book2)
    lb.add(book1)
    lb.show_all()
    lb.remove(book1)
    lb.show_all()