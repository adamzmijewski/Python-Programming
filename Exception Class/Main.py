selection = input("Enter any key to continue or \'q\' to quit:")

while selection != "q":
    try:
        numerator = input("Enter a number for the numerator:")
        denominator = input("Enter a number for the denominator:")
        
        # SPECIALLY DEFINED ERROR FOR ALPHA VARIABLE ENTRY
        if(numerator.isalpha() or denominator.isalpha()):
            raise TypeError("ERROR: Enter a number")
        ratio = float(numerator)/float(denominator)
        
        print("The ratio of the two is %.2f" % (ratio))
    
    # EXCEPTIONS
    except ZeroDivisionError:
        print("ERROR: Division by 0 not allowed")
        
    except TypeError as wordError:
        print(wordError)
        
    except OverflowError:
        print("ERROR: Number too large")
        
    selection = input("\nEnter any key to continue or \'n\' to quit:")
print("Loop stopped.")