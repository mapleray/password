Password Generator
========

```
                                                  _
 _ __    __ _  ___  ___ __      __ ___   _ __  __| |
| '_ \  / _` |/ __|/ __|\ \ /\ / // _ \ | '__|/ _` |
| |_) || (_| |\__ \\__ \ \ V  V /| (_) || |  | (_| |
| .__/  \__,_||___/|___/  \_/\_/  \___/ |_|   \__,_|
|_|

```

# Algorithm

1. `hmac(key, sha512(email)+web, sha512)` ---> `hex string`.
2. `hex string` ---> `binary array` (7bit for each group, use leading zero to keep binary's width is 512bits).
3. Convert element in `binary array` to ASCII character in range(`DECIMAL 33` to `DECIMAL 126`).
4. Generate `15*5` matrix and choose your password according to your own order.
