import pikepdf
import time

pdf_file = input("PDF: ")

passwordList = input("password list: ")
passwords = open(passwordList)

f = 0
i = 0
start_time = time.time()
end_time = 0
for password in passwords:
    password = password.strip("\n")

    
    i += 1
    #print("\r {} Password tested ".format(i), end = "")
    try:
        pikepdf.open(pdf_file, password = password)

        print("\n\n" + "* " *20)

        end_time = time.time()
        print("Password Found! ")
        print("Password is: {}".format(password))
        print("[{}] Password tested in {} seconds".format(i, str(end_time - start_time)[:4]))

        print("* "*20)

        f=1

        passwords.close()
        break
    except:
        end_time = time.time()
        pass

if(f==0):
    print("\nPassword not Found.")
    print("[{}] Password tested in {} seconds".format(i, str(end_time - start_time)[:4]))
