class Account:
    def __init__(self,name,balance):
        self.__name = name
        self.__balance = balance
    @property   
    def name(self):
        return self.__name
    
    @property
    def balance(self):
        return self.__balance
    
    @name.setter
    def name(self,name):
        self.__name = name

    @balance.setter
    def balance(self,balance):
        if balance < 0 :
            print('invalid amount / amount lesser than zero')
        else:
            self.__balance = balance


def main():
  a1 =  Account('ram',10000)
  print(a1.name,a1.balance)
  a1.name = 'sita'
  a1.balance = 100000
  print(a1.name,a1.balance)
  

if __name__ =='__main__':
    main()
        