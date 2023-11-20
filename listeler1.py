liste1=["ali","mehmet","recep","alperen"]
liste2=["emre","alparslan","doğukan","enes"]
while True:
        isim=input("isim giriniz çıkmak için q bas ")
        if isim =="q":
                break
        if isim in liste1:
                print("yukarı kata")
        elif isim in liste2:
                print("aşağı kata")
        elif isim not in liste1 and isim not in liste2:
                print("İsiminiz listede yoktur...")
