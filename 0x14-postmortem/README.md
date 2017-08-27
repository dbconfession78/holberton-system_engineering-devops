Holbert School - 0x11. Postmortem

## Issue Summary
***On 08/24/17 between ~12:00 and 1:40 PM PST***:

s-tickystudios.online ceased authenticating secure private https connections with a valid SSL certificate. 100% of users navigating to https://www.s-tickystudios.online/hbnb/index.html were presented with the browser message, "Your connection is not private". Those who proceeded, did so without a secure private connection.

***Root Cause***: SSL certificate expired without an initial renewal policy in place.
***Business impact***: expired SSL certificate detered 65% of users presented with their browser's insecure connection warning message.

## Timeline
***1:00 PM PST***: issue detected when customer service recived an email reporting the browser message "Your connection is not private." Customer service rep. proceeded to escalate issue to webdev security department.

***1:10 PM PST***: Suspicion of expired SSL confirmed after checking certificate exp. date 
***1:15 PM PST***: temporarily redirected all traffic to webserver, 108-web-01
***1:25 PM PST***: SSL renewed - on load balance server, 108-lb-01:
	 		 	 - stop HAProxy from lsitening on port 80
	 		 	 - run 'certbot certonly --standalone --preferred-challenges http --http-01-port 80 -d s-tickystudios.online -d www.s-tickystudios.online'
				 - verify replacement .pem files in /etc/letsencrypt/live/s-tickystudios.online
				 - combine fullchain.pem and privkey.pem by running 'DOMAI=s-tickystudios.online' sudo -E bash -c 'cat /etc/letsencrypt/live/$DOMAIN/fullchain.pem /etc/letsencrypt/live/$DOMAIN/privkey.pem > /etc/haproxy/certs/$DOMAIN.pem'
				 - set HAProxy to listen on port 80 again

***1:40 PM PST***: traffic redirected back to load balance server, 108-lb-01.
***1:50 PM PST***: tests run and confirmed to ensure subsequent private connections

## Corrective/Preventative meausures taken
Daily certificate auto-renewal policy implemented by:

***1) Creating an executable renewal script***
File: /usr/local/bin/renew.sh

		#!/bin/sh

		SITE=s-tickystudios.online

		# move to the correct let's encrypt directory
		cd /etc/letsencrypt/live/$SITE

		# cat files to make combined .pem for haproxy
		cat fullchain.pem privkey.pem > /etc/haproxy/certs/$SITE.pem

		# reload haproxy
		service haproxy reload
  	 
***2) Updating certbot configuartion***
   - configure letsencrypt to not use port 80 or 443 when renewing. This is done by
editing  /etc/letsencrypt/renewal/s-tickystudios.online.conf at line 'http01_port' to read `http01_port = 54321`
   - after saving, close and test by running `certbot renew --dry-run`

***3) Create a Cron job to run renew.sh every day***
   - run `crontab -e`
   - add the following to the bottom of the file:
  `30 2 * * * /usr/bin/certbot renew --renew-hook "/usr/local/bin/renew.sh" >> /var/log/le-renewal.log`


After the above measures have been taken, further care will be taken by implementing the following:
	- an auto-check script for certificate validity
	- minute-by-minute auto-request to ensure connections are secure and private
        - auto-notifiction (email/text) script for various server events including secure connection fail 
	- a backup script which checks to make sure the cron job has renewed. In the event that a certificate expires anyway this script should run the renew.sh file and use the mentioned notification script to notify admin.

