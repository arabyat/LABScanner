import platform
import os
import time
import sys
from subprocess import Popen
from socket import *
import time

devnull = open(os.devnull, 'wb')

ipscanner_ico = '''                                                                                         
                                                                               
              ###                                 ###                            
              .#*                                /(#                             
                  ##          ######           #/                                
                    #   %     ######(     %  /#                                  
                      #######################                                    
                     #########################                                   
                      #######################                                 
                      ###   ##########   ###                            
                     ###  ### ####### ### ###,                     
                  ######  ## ######## ### #######                       
                  ########  ###########  ########       ##########               
                  ###############################      ###########               
     ##############/ ##############  ##############% ###############             
     ##############/ ##############  ##############% ###############             
     #####     ####/ #####           #####           #####               
####################################  ##############% #####                       
 ##################################  ##############% #####                       
   ################################  ##############% #####                       
     ##### #######   #####                     ####% #####***********            
     #####   ######/ ##############  ##############% ##################          
 
	########################################################
	#               LOCAL NETWORK IP SCANNER               #
	######################################################## 
	#########################################################
	#               Take RESC or lose chance!               #                       
	#########################################################'''
print (ipscanner_ico)

star = "**********************************************************************"

print (star)

ip_range = raw_input("Enter this part of your IP ( example: 192.168.0 ) ---> ")

print (star)
#print "Your IP range ",ip_araligi_deger 
print (star)
if ip_range == "":
	print (star)
	print ("Try to get a valid ip...")
	print (star)
p = []
active = 0
act_ip = []
no_answer = 0
passive = 0
dev_scanned = 0

print ("Scanning IPs ...")
for i in range(0,255):
	ip = ip_range + ".%d" % i
	p.append((ip, Popen(['ping', '-c', '3', ip], stdout=devnull)))
	
while p:
	for i, (ip, proc) in enumerate(p[:]):
		if proc.poll() is not None:
			p.remove((ip, proc))
			if proc.returncode == 0:
				print('%s ACTIVE' % ip)
				act_ip.append(ip)
				active = active + 1
				dev_scanned += 1
			elif proc.returncode == 2:
				print('%s IP' % ip)
				act_ip.append(ip)
				active = no_answer + 1
				dev_scanned += 1
			else:
				#print('%s PASSIVE' % ip)
				passive = passive + 1
				dev_scanned += 1
	time.sleep(.04)
devnull.close()

print (star)
print (" RESC LOCAL NETWORK IP SCANNER.")
print (star)
print ("")
print ( "Scanning completed..")
print star
print "Current operating system ",platform.system()," ", os.name
print "Network Status"
print "Hosts scanned: ",dev_scanned
print "Hosts alive  [ ",active," ]"
print (act_ip)
print ""
print (star)
print ("Scanning ports for the alive hosts ...")
print star

for i in range (len(act_ip)):
	target = act_ip[i]
	t_IP = gethostbyname(target)
	print ('Starting scan on host: ', t_IP)

	for i in range(50, 500):
		s = socket(AF_INET, SOCK_STREAM)

		conn = s.connect_ex((t_IP, i))

		if(conn == 0) :
			print ('Port %d: OPEN' % (i,))
		s.close()

