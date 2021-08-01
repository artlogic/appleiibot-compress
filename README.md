# appleiibot-compress

Unicode compress tweets to https://twitter.com/AppleIIBot

## Install

`pipenv install`

The only external dependency is `unidecode` - it can also just be installed via `pip` if you like.

## Using

``` sh
$ pipenv run python compress.py example.bas

Original length: 263
Compressed length: 255

1FORI=0TO130:POKE885+I,4*PEEK(2125+I)-192+(PEEK(2256+I/3)-35)/4^(I-INT(I/3)*3):NEXT
2&",=n9D`V/QmYnHlX1OnQ8YlB25AnR8J#N9261nV6EmAn8e,k1Z0CT/Z18IlR83nR,긷WnXOn,`X#XT,k0j_E_B1DQ0ٍϬ/QbNo8@B>mJ>mJ>mJ8@BFm2026BnBk=ѬHCJ0S+4'HN?-/@WC#4$6¤%+%CLMCW6#'`%BYMP㏙P-@6%0
```

*example.bas comes from http://www.deater.net/weave/vmwprod/appleiibot/part3.html*

## Limitations

* This is beta quality code. There are likely bugs.
* The compressed length does not take into account Twitter's character weights. Expect slightly higher character counts on Twitter.
