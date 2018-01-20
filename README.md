# ACM's Cloud Computing Workshop
## Setup
- An account with Amazon Web Services (https://console.aws.amazon.com)
- A twitter account for the Twitter Bot application we'll be deploying


## Instructions
1. Sign into your Amazon Web Services (AWS) account
2. Click Services --> Lightsail
3. Press _create instance_
4. Choose the options (us-west-2, linux/ubuntu, Node.js, $5/month)


## Connecting Using SSH (optional, but recommended!)
_Note: This option will only work for Mac & Linux, unless you have PuTTY installed on your windows machine_
1. Visit the Lightsail home page (https://lightsail.aws.amazon.com)
2. Press the _Account_ button
3. Go to SSH Keys
4. Scroll down, and press the _Download_ button corresponding to _Default_
5. Move the .pem file from your downloads to your user account's .ssh folder (in my example I assume that all your 
downloads go to your user's download folder)
    ```bash
    $ mv ~/Downloads/LightsailDefaultPrivateKey-us-west-2.pem ~/.ssh/ 
    ```
6. Change the permissions on your private key so that only _you_ are allowed to read from it
    ```bash
    $ cd ~/.ssh
    $ chmod 400 LightsailDefaultPrivateKey-us-west-2.pem
    ```
7. SSH into your instance by using the public IP of your instance
    ```bash
    $ cd ~/.ssh
    $ ssh -i LightsailDefaultPrivateKey-us-west-2.pem bitmani@34.216.141.44
    ```


## Deploying an Example React.js Application
1. Go to Lightsail, click on your instance, then click on the _Networking_ tab
2. Scroll down to _Firewall_ then add another _Custom_ application using the _TCP_ protocol on port _3000_
2. SSH into your instance or use Lightsail's browser-based remote desktop (RDP) client
3. Clone this workshop's repository
    ```bash
    $ git clone https://github.com/SCUACM/cloud-computing-tutorial.git
    ```
4. Install the necessary packages, then run the application!
    ```bash
    $ cd ~/cloud-computing-tutorial/reactjs-app
    $ npm install
    $ npm start
    ```
5. Open your browser, then paste in your instance's IP with _:3000_ appended to it! (For example, 
http://34.216.141.44:3000/)


## Deploying an Example Twitter Bot
1. Log onto https://apps.twitter.com/ and press _Create New App_
2. Fill out the form, then press _Create your Twitter application_
3. Press on the _Keys and Access Tokens_ tab
4. Scroll down and click _Create my access token_ 
5. SSH into your instance or use Lightsail's browser-based remote desktop (RDP) client
6. Clone this workshop's repository (skip this step if you already did it for the last application)
    ```bash
    $ git clone https://github.com/SCUACM/cloud-computing-tutorial.git
    ```
7. Create a ```keys.json``` file with the keys and access tokens you just created. When finished, save and quit by 
pressing ```esc``` then ```:wq``` then ```enter```
    ```bash
    $ cd ~/cloud-computing-tutorial/python-app
    $ vi keys.json
    ```
    ```json
    {
        "consumer_key": "__your key here__",
        "consumer_key_secret": "__your key here__",
        "access_token": "256240540-__your key here__",
        "access_token_secret": "__your key here__"
    }
    ```
7. Download *pip* which is a package management system used to install and manage software packages written in Python
    ```bash
    $ curl https://bootstrap.pypa.io/get-pip.py > get-pip.py
    $ sudo python get-pip.py
    ```
8. Now we'll download Tweepy, an easy-to-use Python library for accessing the Twitter API
    ```bash
    $ sudo pip install tweepy
    ```
9. Once that's finished, you can go ahead and run your ```tweetbot.py```! If you want to change the keyword you're 
searching for, you can change the ```keywords``` variable inside the python file!
    ```bash
    $ cd ~/cloud-computing-tutorial/python-app
    $ python tweetbot.py
    ```

## Resources
- [Getting Started with Lightsail](https://linuxacademy.com/howtoguides/posts/show/topic/12662-getting-started-with-lightsail-a-simple-vps-solution-from-aws)