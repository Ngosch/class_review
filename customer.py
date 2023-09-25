# 課題C-1: フルネームを取得できる
# 定義: Customerクラス
class Customer:
    # 初期化メソッド
    def __init__(self, first_name, family_name):
        self.first_name = first_name  # 名前
        self.family_name = family_name  # 姓
        
    # フルネームを取得するメソッド
    def full_name(self):
        return f"{self.first_name} {self.family_name}"  # フルネームを返す

# テスト
ken = Customer(first_name="Ken", family_name="Tanaka")
print(ken.full_name())  # "Ken Tanaka" という値を返す

tom = Customer(first_name="Tom", family_name="Ford")
print(tom.full_name())  # "Tom Ford" という値を返す

# 課題C-2のコード（課題C-1 + 課題C-2）
class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

# テスト
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
print(ken.full_name())  # "Ken Tanaka"
print(ken.age)  # 15

tom = Customer(first_name="Tom", family_name="Ford", age=57)
print(tom.full_name())  # "Tom Ford"
print(tom.age)  # 57

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
print(ieyasu.full_name())  # "Ieyasu Tokugawa"
print(ieyasu.age)  # 73

# 課題C-3のコード（課題C-1 + C-2 + C-3）
class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    def entry_fee(self):
        if self.age < 20:
            return 1000
        elif 20 <= self.age < 65:
            return 1500
        else:
            return 1200

# テスト
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
print(ken.entry_fee())  # 1000

tom = Customer(first_name="Tom", family_name="Ford", age=57)
print(tom.entry_fee())  # 1500

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
print(ieyasu.entry_fee())  # 1200
