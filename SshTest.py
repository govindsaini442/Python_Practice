import paramiko
f = open("test2.txt","w")
f1 = open("test2.txt","r")
hostname = "18.188.25.138"
myuser   = "ubuntu"
mySSHK   = "C:/Users/Govind/Downloads/Coaching_Docs/Ubuntu_Key.pem"
command = "df -HT"
sshcon   = paramiko.SSHClient()  # will create the object
sshcon.set_missing_host_key_policy(paramiko.AutoAddPolicy())# no known_hosts error
sshcon.connect(hostname, username=myuser, key_filename=mySSHK)
stdin,stdout,stderr=sshcon.exec_command(command)
outlines=stdout.readlines()
resp=''.join(outlines)
f.write(resp)
f.close()
#print(resp)
data=f1.readlines()
for lines in data:
    print(lines.replace("     ",","))
