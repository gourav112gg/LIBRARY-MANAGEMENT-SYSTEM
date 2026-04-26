from add_books import add
from issue_books import issue
from show_books import show
from return_books import return_book

def library():
    print("Welcome To Library")
    while True:
        print("\n1.Add book")
        print("\n2.show book")
        print("\n3.Issue book")
        print("\n4.Return book")
        print("\n5.Exit")
        choice = int(input("Enter your choice:"))

        if choice==1:   add()
        elif choice==2: show()
        elif choice==3: issue()
        elif choice==4: return_book()
        elif choice==5: 
            print("Thank you")
            break
        else:
            print("Invalid choice")