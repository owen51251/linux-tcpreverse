import msvcrt, sys, os


li = []
def pass_shield():
    while 1:
        ch = msvcrt.getch()
        #循環
        if ch == b'\r':
            msvcrt.putch(b'\n')
            return b''.join(li).decode()
        #退格
        elif ch == b'\x08':
            if li:
                li.pop()
                msvcrt.putch(b'\b')
                msvcrt.putch(b' ')
                msvcrt.putch(b'\b')
        #Esc
        elif ch == b'\x1b':
            break
        else:
            li.append(ch)
            msvcrt.putch(b'*')
    
password=pass_shield()
print (password)