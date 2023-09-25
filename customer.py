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
# 定義: Customerクラス
class Customer:
    # 初期化メソッド
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name  # 名前
        self.family_name = family_name  # 姓
        self.age = age  # 年齢
        
    # フルネームを取得するメソッド
    def full_name(self):
        return f"{self.first_name} {self.family_name}"  # フルネームを返す

# テスト
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
print(ken.full_name())  # "Ken Tanaka" という値を返す
print(ken.age)  # 15 という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age=57)
print(tom.full_name())  # "Tom Ford" という値を返す
print(tom.age)  # 57 という値を返す
