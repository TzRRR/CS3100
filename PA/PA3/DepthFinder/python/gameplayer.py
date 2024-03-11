# Tianze Ren, tr2bx
def playgame_dc(gb, left, right):
    if right - left < 2:
        if gb.ping(left) > gb.ping(right):
            return left
        else:
            return right
    else:
        onethird = left + (right - left) // 3
        twothird = right - (right - left) // 3
        one = gb.ping(onethird)
        two = gb.ping(twothird)
        if two > one:
            return playgame_dc(gb, onethird+1, right)
        elif two < one:
            return playgame_dc(gb, left, twothird-1)

