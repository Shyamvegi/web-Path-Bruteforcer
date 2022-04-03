# cloudsek_BE
# CloudSEK SDE Task Using Python
	-It consists the actual implementation of web path brute forcer
    -It works on threading
    -fast and minimal cpu usage

## clone the repository using
```sh
$ git clone "git-url"
```

## Now run requirements file to install all dependencies 

```sh
(env)\pip install -r requirements.txt
```      

web app URL
A file containing a list of web app paths that need to be brute-forced against the specified web app URL  [Minimum paths: 1000]Sample wordlist:
Sample wordlist: Link
List of success status code: (default:  [200])
Sample Input:

Webapp url: https://www.github.com

Webapp paths: sample 5 lines out of 1000 of the input file wordlist.txt

●      admin

●      info

●      .git/config

●      .htaccess

●      backup.zip

Success status codes: [200, 302]


 

Sample Output: A list of URLs that responded with any of the success status codes as provided in the input by the user.
 

●      https://www.github.com/info [Status code 302]

●      https://www.github.com/.htaccess [Status code 200]


-"Screenshot"
![](/result.png)