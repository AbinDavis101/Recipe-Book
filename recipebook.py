view=["sambar","beef fry","choor","pork fry","biriyani","chicken curry","fried rice","french fries"]
flag=True
def new():
    global view
    a=input("Enter the name of the recipe : ")
    view.append(a)
    print("recipes")
    for i in view:
        print("    ",i)
    print(a," has been added to the recipe book")
def search():
    global view
    b=input("Enter the recipe you want to search ")
    if b in view:
        print("Recipe Found",b)
    else:
        print("Recipe is not in the book " )
while flag==True:
    print("RECIPE BOOK")
    print("___________")
    print("1.View all the Recipes")
    print("2.Search for a Recipe")
    print("3.Add a New Recipe")
    print("4.Exit")
    c=int(input("Enter your choice : "))
    if c==1:
        print("recipes")
        for d in view:
            print("     ",d)
    elif c==2:
        search()
    elif c==3:
        new()
    elif c==4:
        flag=False

# with open("new recipe.txt","w") as new:
#     new.write("")

        