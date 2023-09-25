# 課題C-1: フルネームを取得できる
print("------------------課題C-1----------------------")
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
print("------------------課題C-2----------------------")
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
print("------------------課題C-3----------------------")
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


# 課題C-4のコード（課題C-1 + C-2 + C-3 + C-4）
print("------------------課題C-4----------------------")
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

    def info_csv(self):
        return f"{self.full_name()},{self.age},{self.entry_fee()}"


# テスト
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
print(ken.info_csv())  # "Ken Tanaka,15,1000"

tom = Customer(first_name="Tom", family_name="Ford", age=57)
print(tom.info_csv())  # "Tom Ford,57,1500"

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
print(ieyasu.info_csv())  # "Ieyasu Tokugawa,73,1200"

# 課題C-5のコード（課題C-1 + C-2 + C-3 + C-4 + C-5）
print("------------------課題C-5----------------------")
class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    def entry_fee(self):
        if self.age <= 3:
            return 0
        elif self.age < 20:
            return 1000
        elif 20 <= self.age < 65:
            return 1500
        else:
            return 1200

    def info_csv(self):
        return f"{self.full_name()},{self.age},{self.entry_fee()}"

# テスト
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
print(ken.info_csv())  # "Ken Tanaka,15,1000"

tom = Customer(first_name="Tom", family_name="Ford", age=57)
print(tom.info_csv())  # "Tom Ford,57,1500"

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
print(ieyasu.info_csv())  # "Ieyasu Tokugawa,73,1200"

baby = Customer(first_name="Taro", family_name="Yamada", age=2)
print(baby.info_csv())  # "Taro Yamada,2,0"

# 課題C-6のコード（課題C-1 + C-2 + C-3 + C-4 + C-5 + C-6）
print("------------------課題C-6----------------------")
class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    def entry_fee(self):
        if self.age <= 3:
            return 0
        elif self.age < 20:
            return 1000
        elif 20 <= self.age < 65:
            return 1500
        elif 75 <= self.age:
            return 500
        else:
            return 1200

    def info_csv(self):
        return f"{self.full_name()},{self.age},{self.entry_fee()}"

# テスト
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
print(ken.info_csv())  # "Ken Tanaka,15,1000"

tom = Customer(first_name="Tom", family_name="Ford", age=57)
print(tom.info_csv())  # "Tom Ford,57,1500"

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
print(ieyasu.info_csv())  # "Ieyasu Tokugawa,73,1200"

baby = Customer(first_name="Taro", family_name="Yamada", age=2)
print(baby.info_csv())  # "Taro Yamada,2,0"

elderly = Customer(first_name="Jiro", family_name="Sato", age=80)
print(elderly.info_csv())  # "Jiro Sato,80,500"

# 課題C-7のコード（課題C-1 + C-2 + C-3 + C-4 + C-5 + C-6 + C-7）
print("------------------課題C-7----------------------")
class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    def entry_fee(self):
        if self.age <= 3:
            return 0
        elif self.age < 20:
            return 1000
        elif 20 <= self.age < 65:
            return 1500
        elif 75 <= self.age:
            return 500
        else:
            return 1200

    def info_csv(self):
        return f"{self.full_name()},{self.age},{self.entry_fee()}"

    def info_tab(self):
        return f"{self.full_name()}\t{self.age}\t{self.entry_fee()}"

# テスト
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
print(ken.info_tab())  # "Ken Tanaka  15  1000"

tom = Customer(first_name="Tom", family_name="Ford", age=57)
print(tom.info_tab())  # "Tom Ford    57  1500"

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
print(ieyasu.info_tab())  # "Ieyasu Tokugawa  73  1200"

baby = Customer(first_name="Taro", family_name="Yamada", age=2)
print(baby.info_tab())  # "Taro Yamada  2  0"

elderly = Customer(first_name="Jiro", family_name="Sato", age=80)
print(elderly.info_tab())  # "Jiro Sato  80  500"

# 課題C-8のコード（課題C-1 + C-2 + C-3 + C-4 + C-5 + C-6 + C-7 + C-8）
print("------------------課題C-8----------------------")
class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    def entry_fee(self):
        if self.age <= 3:
            return 0
        elif self.age < 20:
            return 1000
        elif 20 <= self.age < 65:
            return 1500
        elif 75 <= self.age:
            return 500
        else:
            return 1200

    def info_csv(self):
        return f"{self.full_name()},{self.age},{self.entry_fee()}"

    def info_tab(self):
        return f"{self.full_name()}\t{self.age}\t{self.entry_fee()}"

    def info_psv(self):
        return f"{self.full_name()}|{self.age}|{self.entry_fee()}"

# テスト
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
print(ken.info_psv())  # "Ken Tanaka|15|1000"

tom = Customer(first_name="Tom", family_name="Ford", age=57)
print(tom.info_psv())  # "Tom Ford|57|1500"

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
print(ieyasu.info_psv())  # "Ieyasu Tokugawa|73|1200"

baby = Customer(first_name="Taro", family_name="Yamada", age=2)
print(baby.info_psv())  # "Taro Yamada|2|0"

elderly = Customer(first_name="Jiro", family_name="Sato", age=80)
print(elderly.info_psv())  # "Jiro Sato|80|500"
