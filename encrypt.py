#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 ubuntu <ubuntu@ubuntu>
#
# Distributed under terms of the MIT license.
import hashlib
import hmac


def splitline(s, length):
    return [s[0 + i:length + i] for i in range(0, len(s), length)]


def generate(email, web, key):
    h = hmac.new(key, hashlib.sha512(email).hexdigest() + web, hashlib.sha512)
    k = h.hexdigest()
    # keep leadding zero
    b = format(int(k, 16), '0512b')
    # b = bin(int(k, 16)).partition('b')[2]
    chs = splitline(b, 7)

    ret = [chr(int(ch, 2) % 94 + 33) for ch in chs]

    for i in splitline(ret, 15):
        print ''.join(i)


if __name__ == '__main__':
    email = 'email'
    web = 'web'
    key = 'key'

    generate(email, web, key)
