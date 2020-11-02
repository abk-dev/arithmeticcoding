Ac_dictionary = {                   # Commutative Distribution Function (CDF) values for their Probabilities
    "0": 0,
    " ": 0.1686,
    "A": 0.2328,
    "B": 0.2455,
    "C": 0.2673,
    "D": 0.299,
    "E": 0.4021,
    "F": 0.4229,
    "G": 0.4381,
    "H": 0.4848,
    "I": 0.5423,
    "J": 0.5431,
    "K": 0.548,
    "L": 0.5801,
    "M": 0.5999,
    "N": 0.6546,
    "O": 0.7178,
    "P": 0.733,
    "Q": 0.7338,
    "R": 0.7822,
    "S": 0.8336,
    "T": 0.9332,
    "U": 0.956,
    "V": 0.9643,
    "W": 0.9818,
    "X": 0.9831,
    "Y": 0.9995,
    "Z": 1
}
while 1:
    up = [""]       # Upper Limit values array
    lo = [""]       # Lower Limit Values Array
    tm = [""]       # For Decipher tag value
    up[0]= 1
    lo[0]= 0
    x = 1
    sentence = input('Enter the Sentence:')         # Input Sentence From User
    block_length_min = int(input("Enter Block length starting index: "))
    block_length_max = int(input("Enter Block length ending index: "))          # Block length
    for letter in range(block_length_min, block_length_max+1):
        if sentence[letter] in Ac_dictionary:
            up.append(lo[x - 1] + (up[x - 1] - lo[x - 1]) * (Ac_dictionary.get(sentence[letter])))  # Upper Limit Formula
            lo.append(lo[x - 1] + (up[x - 1] - lo[x - 1]) * (list(Ac_dictionary.values())[(list(Ac_dictionary.keys()).index(sentence[letter])) - 1]))  # Lower Limit Formula
        x += 1


    print("UpperLimit Values are given below")
    print(up)
    print("LowerLimit Values are given below")
    print(lo)

    print("Its tag value is given below")
    tag_value = (up[-1]+lo[-1])/2               # -1 in argument gives the value of last element in array
    print(tag_value)

# To Decipher code
    arr = [""]
    arr[0]= 0
    tm[0] = tag_value            # 1st value of tm when k = 1
    y=2                          # For 2nd value of tm when k = 2
    for tag in range(block_length_min+1, block_length_max+1):
        tm.append((tag_value-lo[y-1])/(up[y-1]-lo[y-1]))            # tm equation formula
        y += 1
    print("Tm value ", tm)

    limit = (block_length_max-block_length_min)+1
    for a in range(0, limit):
        for b in range(0, 27):
            if (list(Ac_dictionary.values())[b]) > tm[a] > (list(Ac_dictionary.values())[b - 1]):
                arr.append(list(Ac_dictionary.values())[b])
    print("array", arr)      # array of values of Alphabets
    print("Our Original sequence is given below")
    for index in range(1, limit+1):     # As arr Array first element is zero so starts it on 1st index
        for orignal_letter in range(0, 27):
            if arr[index] == (list(Ac_dictionary.values())[orignal_letter]):
                print(list(Ac_dictionary.keys())[list(Ac_dictionary.values()).index(arr[index])])

