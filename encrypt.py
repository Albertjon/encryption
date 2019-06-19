import os

def main():
    keys = []                                       
    with open("key_generator.txt", 'r') as file:
        for line in file:
            for a in line.split():                  
                
                keys.append(a)                      
    n = int(keys[2])                                
    e = int(keys[4])                                
    s = str(input("enter a filename: "))
    encrypted_mess = open(s+".enc", 'w')     
    with open(s, ) as newFile:
        for word in newFile:
            for char in word:
                print(encryption(ord(char),e,n),file=encrypted_mess)    
    
    os.remove(s)
    
    print(n, file=encrypted_mess)                              
    print(keys[4], file=encrypted_mess)

#encyrption funciton. m^e % n
def encryption(m,e,n):
    x = pow(m,e,n)
    return x

main()