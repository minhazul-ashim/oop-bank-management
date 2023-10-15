from SystemInteraction import SystemInteraction;

while True :
    print('\n Choose your Option');
    print('1 - Interact as User');
    print('2 - Interact as Admin');
    print('3 - Terminate Process');
    print('Go to', end=" ");
    n = int(input());
    if n == 1 :
        while True :
            print('Choose your Option');
            print('1 - Create Account');
            print('2 - Log in to Existing Account');
            print('Go to ', end=" ");
            x = int(input());
            if x == 1 :
                SystemInteraction.accountCreation();
            elif x == 2 :
                pass;
            else :
                print('Invalid Option');
    elif n == 2 :
        pass;
    elif n == 3 :
        print('Process Terminated');
        break;