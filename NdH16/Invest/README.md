# Invest

## Introduction

This was my first CTF challenge ever. It was fun and easier than it seemed. I
think statically speaking not a lot of people did. If I remember right it was
way less than 100.

### Description

A paranoid guy seems to have secured his file very well. But I am convinced he
made a mistake somewhere...

The challenge is available at : http://static.quals.nuitduhack.com/invest.pcapng

### Details

```
Points    50
Category  Inforensic
```

## The resolving

We were given a ```.pcapng``` file and that's all. So let's fire up Wireshark
and dive into it.

The file seems to contain an HTTP exchange. Since it is not a HTTPS one using it
is really easy. Wireshark offers a lot of great tools for that.

```
-> File
  -> Export Objects
    -> HTTP
```

This tool will follow the TCP dialogue and rebuild exchanged files. In this case
it gives us a lot of files. Let's gather them all and analyse them.

### Files

```
$ ls -lah
total 532K
drwxr-xr-x 2 rhinoceros rhinoceros 4.0K Apr  3 12:42 .
drwxr-xr-x 3 rhinoceros rhinoceros 4.0K Apr  3 12:42 ..
-rw-r--r-- 1 rhinoceros rhinoceros  56K Apr  3 12:42 12767348_10208095326368148_1014857467_n.jpeg
-rw-r--r-- 1 rhinoceros rhinoceros  934 Apr  3 12:42 %2f
-rw-r--r-- 1 rhinoceros rhinoceros  934 Apr  3 12:42 %2f(1)
-rw-r--r-- 1 rhinoceros rhinoceros  216 Apr  3 12:42 back.gif
-rw-r--r-- 1 rhinoceros rhinoceros  17K Apr  3 12:42 chall
-rw-r--r-- 1 rhinoceros rhinoceros  17K Apr  3 12:42 chall(1)
-rw-r--r-- 1 rhinoceros rhinoceros  17K Apr  3 12:42 chall(2)
-rw-r--r-- 1 rhinoceros rhinoceros 1.3K Apr  3 12:42 encryptaa

  ...

-rw-r--r-- 1 rhinoceros rhinoceros 1.3K Apr  3 12:42 encryptdb
-rw-r--r-- 1 rhinoceros rhinoceros   65 Apr  3 12:42 encryptdc
-rw-r--r-- 1 rhinoceros rhinoceros    2 Apr  3 12:42 hotspot(1).txt
-rw-r--r-- 1 rhinoceros rhinoceros    2 Apr  3 12:42 hotspot.txt
-rw-r--r-- 1 rhinoceros rhinoceros  309 Apr  3 12:42 image2.gif
-rw-r--r-- 1 rhinoceros rhinoceros 1.6K Apr  3 12:42 key
-rw-r--r-- 1 rhinoceros rhinoceros  769 Apr  3 12:42 key.txt
-rw-r--r-- 1 rhinoceros rhinoceros 7.5K Apr  3 12:42 poop.jpeg
-rw-r--r-- 1 rhinoceros rhinoceros  229 Apr  3 12:42 text.gif
-rw-r--r-- 1 rhinoceros rhinoceros  245 Apr  3 12:42 unknown(1).gif
-rw-r--r-- 1 rhinoceros rhinoceros  245 Apr  3 12:42 unknown.gif
-rw-r--r-- 1 rhinoceros rhinoceros  31K Apr  3 12:42 wp
```

Let's take them one by one, the description is under the filename:

```
-rw-r--r-- 1 rhinoceros rhinoceros  56K Apr  3 12:42 12767348_10208095326368148_1014857467_n.jpeg
```
A screenshot of a logical circuit. Strange to find something like this.

```
-rw-r--r-- 1 rhinoceros rhinoceros  934 Apr  3 12:42 %2f
-rw-r--r-- 1 rhinoceros rhinoceros  934 Apr  3 12:42 %2f(1)
```
HTML files. Some kind of repository tree, ftp-style. No informations here.

```
-rw-r--r-- 1 rhinoceros rhinoceros  216 Apr  3 12:42 back.gif
-rw-r--r-- 1 rhinoceros rhinoceros  309 Apr  3 12:42 image2.gif
-rw-r--r-- 1 rhinoceros rhinoceros  229 Apr  3 12:42 text.gif
-rw-r--r-- 1 rhinoceros rhinoceros  245 Apr  3 12:42 unknown(1).gif
-rw-r--r-- 1 rhinoceros rhinoceros  245 Apr  3 12:42 unknown.gif
```
Gif used to decorate HTML pages.

```
-rw-r--r-- 1 rhinoceros rhinoceros  17K Apr  3 12:42 chall
-rw-r--r-- 1 rhinoceros rhinoceros  17K Apr  3 12:42 chall(1)
-rw-r--r-- 1 rhinoceros rhinoceros  17K Apr  3 12:42 chall(2)
```
Another file listing. It just lists ```encryptXX``` files.

```
-rw-r--r-- 1 rhinoceros rhinoceros 1.3K Apr  3 12:42 encryptaa

  ...

-rw-r--r-- 1 rhinoceros rhinoceros 1.3K Apr  3 12:42 encryptdb
-rw-r--r-- 1 rhinoceros rhinoceros   65 Apr  3 12:42 encryptdc
```
Ah something fishy! A file which has been splitted with ```split``` command.
Well it looks like so. From ```split``` man pages:
```
Output  fixed-size pieces of INPUT to PREFIXaa, PREFIXab, ...;
```

```
-rw-r--r-- 1 rhinoceros rhinoceros    2 Apr  3 12:42 hotspot(1).txt
-rw-r--r-- 1 rhinoceros rhinoceros    2 Apr  3 12:42 hotspot.txt
```
Theses files just contain "OK". Well, yeah, "OK" ...

```
-rw-r--r-- 1 rhinoceros rhinoceros 1.6K Apr  3 12:42 key
```
Another file listing. But this time it is interesting. We can learn that:
```
-rw-r--r-- 1 rhinoceros rhinoceros  56K Apr  3 12:42 12767348_10208095326368148_1014857467_n.jpeg
-rw-r--r-- 1 rhinoceros rhinoceros  769 Apr  3 12:42 key.txt
```
Come from the same folder. That is important.

```
-rw-r--r-- 1 rhinoceros rhinoceros  769 Apr  3 12:42 key.txt
```
It contains some kind of "binary" message:
```
01000111010111100110001101101110010010010011100101011110010001110100011100111001
01000111001110010100011100111001010001110011100101011110011000110110111001001001
01101110010010010011100100110101010111100110001100111001001101010110111001001001
01101110010010010100011101011110001110010011010101101110010010010101111001100011
01000111010111100011100100110101010111100110001101011110011000110101111001100011
01000111010111100101111001100011011011100100100101000111010111100011100100110101
01000111010111100110111001001001010111100110001101011110011000110110111001001001
01011110011000110101111001100011001110010011010101000111010111100101111001100011
01011110011000110101111001100011010001110101111001000111010111100101111001100011
011011100100100101101110010010010101111001100011
```
Now we are talking !

```
-rw-r--r-- 1 rhinoceros rhinoceros  31K Apr  3 12:42 wp
```
This looks like gibberish. But the header ```json``` and the differents ```%XX```
yield HTML encoding. Well let's keep that in mind.

### encryptXX

It seems pretty obvious that the good stuff is kept inside the ```encryptXX```
files. In order to paste them together:
```
cat encrypt* > global_encrypt
```

A little ```head``` / ```tail``` / ```ls -lah```  control confirm the operation:
```
$ head -n 1 encryptaa
U2FsdGVkX1992IPwJkNauCcPh4kHU5ilGdecrR5qkxBrKD+JsyMh20yhgQLZdyuI

$ head -n 1 global_encrypt 
U2FsdGVkX1992IPwJkNauCcPh4kHU5ilGdecrR5qkxBrKD+JsyMh20yhgQLZdyuI

$ tail -n 1 encryptdc
GHxLtAW8l2jwJ3FGEftSzc4Y+wBLwBC49r02pXTX7U03aUhrltUb1FWls54aAxnn

$ tail -n 1 global_encrypt 
GHxLtAW8l2jwJ3FGEftSzc4Y+wBLwBC49r02pXTX7U03aUhrltUb1FWls54aAxnn

$ ls -lah global_encrypt 
-rw-r--r-- 1 rhinoceros rhinoceros 102K Apr  3 13:04 global_encrypt
```

And this gives another important information: this is a base64 encoded file!
```
$ cat global_encrypt | base64 -r > raw_encrypt
```

```raw_encrypt``` is now some binary gibberish. But it has a interesting
header! :
```
$ cat raw_encrypt | xxd | head -n 1
0000000: 5361 6c74 6564 5f5f 7dd8 83f0 2643 5ab8  Salted__}...&CZ.
```
The firsts bytes represent the word "Salted__". Google helps us out on this one:
>OpenSSL salted format is our name for the file format OpenSSL usually uses when
>writing password-protected encrypted files.
>Files have an 8-byte signature, followed by an 8(?)-byte salt. Following the
>salt is the encrypted data.
>The salt and password are to be combined in a particular way, to derive the
>encryption key and initialization vector.
>No information about which encryption cipher was used is stored in the file. In
>order to decrypt the file, the cipher must be known by external means, or
>guessed. (Obviously, the same goes for the password.) 


>Files begin with an 8-byte signature: the ASCII characters "Salted__". 

From http://justsolve.archiveteam.org/wiki/OpenSSL_salted_format

So what we need :
- the password
- the encryption cypher used

### key.txt
```key.txt``` feels like the right starting point. But it is just some 01. We
could try to translate that into a string with a 8bits per characters basis. I
did not even try because of the logical circuit screenshot.

Take a look at it. 8 entries and the how long is the ```key.txt``` string ?:
```
$ wc -c key.txt
769
```
Ow 769 % 8 = 1. So close. But way there's more !:
```
$ cat key.txt | xxd | tail -n 1
0000300: 0a                                       .
```
That what I thought. The good old trailling ```\x0a```. Now 768 % 8 = 0. This
seems really big to be just a coincidence.

Let's write a script translating the ```key.txt``` with the logical circuit. I
build mine in Python. It is really simple and might not be Pythonic but it
works. You'll find it in the repo ```script.py```.

My script prints out:
- the translated binary key
- the char from every 8bits
- the password string

```
$ python script.py 
001101000101010101101011011110100011100100110101010001100011001001011001011100010101000001101001
('00110100', 52, '4')
('01010101', 85, 'U')
('01101011', 107, 'k')
('01111010', 122, 'z')
('00111001', 57, '9')
('00110101', 53, '5')
('01000110', 70, 'F')
('00110010', 50, '2')
('01011001', 89, 'Y')
('01110001', 113, 'q')
('01010000', 80, 'P')
('01101001', 105, 'i')
4Ukz95F2YqPi
```

#### Translation problem
Here we got lucky because there was no tricky part. But the logical circuit
could have taken the entry much more differently. With an other bit order for
example. And the string at the end could have been in the wrong order,
etc... It would not have been funny to try every possibilities.

### the encryption cypher
Nothing fancy here. I just tried every cypher from my ```openSSL``` package. The
right one was ```aes-256-cbc```.

```
openssl aes-256-cbc -d -in raw_encrypt -out raw_clear
```

### the clear file
The binary header might help us:
```
$ cat raw_clear | xxd | head -n 1
0000000: 504b 0304 1400 0808 0800 b9b2 9c47 0000  PK...........G..
```
https://en.wikipedia.org/wiki/List_of_file_signatures tells us that it might be:
- zip
- jar
- odt
- ods
- odp
- docx
- xlsx
- pptx
- vsdx
- apk

Aaaaand opening it with ```LibreOffice``` works !

### one last trick
The file is just a blank page with a picture saying "Fooled You!". This can't be
true I spend too much time on it!

At least let's verify if there is nothing behind this picture aaaand moving it
reveals the flag! ```NDH[59rRS57bd5WH8RxgPbRS27q89a5bWrjL]```

## Conclusion
This was my first CTF challenge ever. It did not take me a lot of time and there 
were just enough hints to keep me going without being too easy. My first 50
points !
