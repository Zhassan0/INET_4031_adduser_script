#!/usr/bin/python
import os
import re
import sys

def main():
    for line in sys.stdin:
        match=re.match('#', line)
        fields= line.strip().split(':')

        if match or len(fields) !=5:
            continue

        username=fields[0]
        password=fields[1]

        gecos ="%s %s,,," % (fields[3],fields[2])

        groups= fields[4].split(',') #split when you get to ,

        print"==> Creating account for %s..." %(username)

        cmd="/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)
        #print cmd
        os.system(cmd)# executes shell commands
        print "==> Setting the password for %s..." % (username)
        cmd= "/bin/echo -ne '%s\n%s' | /usr/bin/sudo  /usr/bin/passwd %s" % (password,password,username)
        #print cmd
        os.system(cmd)
        for group in groups: #
            if group !='-':
                print "==> Assigning %s to the %s group..." %(username,group)
                cmd ="/usr/sbin/adduser %s %s" % (username,group)
                #print cmd
                os.system(cmd)

if __name__=='__main__':
    main()

