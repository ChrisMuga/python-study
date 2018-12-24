def introduction():
    fname   =   input('First Name: ')
    lname   =   input('Last Name: ')
    name    =   f'{fname} {lname}'

    #use Title Case on name
    name    =   name.title()

    print(f'Welcome, {fname.title()}')
    p       =   float(input('How much would you like to loan?: '))
    r       =   12.5
    print(f'The interest rate is {r}')
    t       =   float(input('Please define loan period(In Years): '))

    #return total
    total   =   simple_interest(p, r, t)
    print(f'{name} will pay KES. {total} in {t} years')

   
def simple_interest(p,r,t):
    interest    =   (p * r * t)/100
    amount      =   interest + p
    #return value
    return amount


introduction()


