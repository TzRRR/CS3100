# Tianze Ren, tr2bx, 03/01/2023
import math

def find_median(c1, c2):
    return find_helper(c1, c2, 0, int((c1.size - 1)/2), c1.size - 1, 0, int((c2.size - 1)/2), c2.size - 1)

def find_helper(c1, c2, l1, m1, r1, l2, m2, r2):
    if (abs(m1 - l1) == 0 or abs(m1 - r1 == 0)) and (abs(m2 - l2) == 0 or abs(m2 - r2 == 0)):
            return (max(c1.request(l1), c2.request(l2)) + min(c1.request(r1), c2.request(r2))) / 2
    else:
        if (l1 - r1 + 1) % 2 == 0:
            if c1.request(m1) > c2.request(m2):
                return find_helper(c1, c2, l1, int((l1 + m1 + 1) / 2), m1 + 1, m2, int((m2 + r2) / 2), r2)
            elif c1.request(m1) < c2.request(m2):
                return find_helper(c1, c2, m1, int((r1 + m1) / 2), r1, l2, int((m2 + l2 + 1) / 2), m2 + 1)
            else:
                return find_helper(c1, c2, m1, m1, m1 + 1, m2, m2, m2 + 1)
        else:
            if c1.request(m1) > c2.request(m2):
                return find_helper(c1, c2, l1, int((l1 + m1) / 2), m1, m2, int((m2 + r2) / 2), r2)
            elif c1.request(m1) < c2.request(m2):
                return find_helper(c1, c2, m1, int((r1 + m1) / 2), r1, l2, int((m2 + l2) / 2), m2)
            else:
                return c1.request(m1)


