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
