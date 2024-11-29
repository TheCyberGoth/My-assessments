def extract_and_rearrange(string):  # Corrected function name
    str_1 = "".join(reversed(string[0:4].replace('g', ''))).capitalize()  
    str_2 = "".join(string[6:13].split('ro'))  
    str_3 = "".join(reversed(list(string[14:20]))).split(string[17])[0]
    
    # Corrected indices and split method
    str_4 = "".join(string[21:29].split(string[23:28]))

    return str_1 + " " + str_2 + " " + str_3 + " " + str_4 + " "

def ultra_extract_and_rearrange(string):  # Corrected function name
    first_transform = extract_and_rearrange(string)
    return first_transform


print(ultra_extract_and_rearrange("egthb quirock nwoGrb forijmpxv"))

