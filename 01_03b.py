def main():
    #Add code here
    inventory = Counter(STA001=10, SAL002=20, ENT004=13)
    sell = Counter(STA001=5, SAL002 = 3, ENT004 = 3)
    make = Counter(STA001 = 9,ENT004 = 1)
    after = inventory - sell + make
    print(after)

if __name__ == "__main__":
    main()