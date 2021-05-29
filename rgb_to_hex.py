"""
Write a function that takes in RGB color values and converts it into the hexadecimal color.
The function should take three arguments for the R, G, and B values. If the R, G, or B values 
are outside of the 0 to 255 range they should be converted to the closest number in that range
"""

def rgb_to_hex(red, green, blue):
    # result = ""
    # for color in [red, green, blue]:
    #     if color > 255: color = 255
    #     hex_color = hex(color)[2:].upper()
    #     result += hex_color.zfill(2)
    # return result

    def hexify(number):
        if number < 0: number = 0
        if number > 255: number = 255
        return hex(number)[2:].upper().zfill(2)

    return "".join(list(map(hexify, [red, green, blue])))

def test_rgb_solution():
    assert rgb_to_hex(255, 255, 255) == 'FFFFFF'
    assert rgb_to_hex(255, 255, 300) == 'FFFFFF'
    assert rgb_to_hex(0, 0, 0) == '000000'
    assert rgb_to_hex(148, 0, 211) == '9400D3'
    assert rgb_to_hex(254,253,252) == "FEFDFC"
    assert rgb_to_hex(220, 67, 368) == "DC43FF"