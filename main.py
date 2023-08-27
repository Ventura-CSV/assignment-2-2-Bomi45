def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celcius fahrenheit 
    ##################################################
    """
    #celcius 23
     
    celcius = int(input("Enter temperature in Celcius: "))
    
    
    fahrenheit = 9/5 * celcius + 32
    
    print(f'Fahrenheit temperature: \t {fahrenheit:.2f}')
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celcius, fahrenheit


if __name__ == '__main__':
    main()
