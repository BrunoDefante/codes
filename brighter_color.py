import numpy as np

def color_bright(color, percent, bright):
    channels = [int(color[i:i+2], 16) for i in range(0, len(color), 2)]
    channels_reduce = [int(channel * percent) for channel in channels]
    if bright == "+":
        final_color = np.add(channels, channels_reduce)
    elif bright == "-":
        final_color = np.subtract(channels, channels_reduce)

    try:
        for channel in final_color:
            if channel > 255:
                raise ValueError("Valor Máximo Excedido!", channel)
    except ValueError as error:
        print(error)
        exit(0)

    final_color = [hex(channel)[2:].upper() for channel in final_color]
    final_color = "".join(final_color)
    return final_color


color = input("Type a Hex Color code: ").upper().replace('#','')
percent = float(input("Type a percent to apply in the color: "))
bright = input('"+" to Increase the bright or "-" to Decrease: ')


final_color = color_bright(color=color, percent=percent, bright=bright)
print(f"A cor #{color} está {percent * 100}% {bright} brilhosa")
print(f"Cor final: #{final_color}")


