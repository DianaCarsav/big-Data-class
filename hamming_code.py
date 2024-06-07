def calculate_parity_bits(m):

    p = 0

    while (2 ** p) < m + p + 1: #mientras p no cumpla la condicion de 2^p>= m+p+1 sume 1 hasta que la cumpla

        p += 1

    return p


def position_parity_bits(data, p):

    j = 0

    k = 1

    m = len(data) 

    result = ''


    for i in range(1, m + p + 1): #aqui cuenta todos los naturales desde 1 hasta el numero de la paridad

        if i == 2 ** j: #compara si el resultado es una potencia de 2

            result += '0'

            j += 1
            print(i)
        else:

            result += data[-k]

            k += 1



        print("Aqui finaliza posicion paridad. result: ", result)
    #return result   
    return result[::-1]



def calculate_parity_values(code, p): #aqui code es el numero binario que resulta de aplicar la funcion position_parity

    n = len(code)
    print("code1: ", code)
    print("aqui inicia calculo de valores de paridad. lengt of codificated word= ",n)
    for i in range(p):
        print(i)
        val = 0
        for j in range(1, n + 1): #recorre los digitos desde 1 hasta n que es la logitud final de la palabra codificada

            if j & (2 ** i) == (2 ** i): #estoy haciendo un and en binario. es decir aqui toma los j(j es la posicion dentro de la palabra codificada) en binario

                val = val ^ int(code[-j]) #xor -j la salida es verdadera si las entradas no son iguales, de otro modo el resultado es falso
            print("val",val)    
            print("code: ", code)
            print("si j=",str(j),"entonces val= ", val)
        code = code[:n-(2**i)] + str(val) + code[n-(2**i)+1:] #[-1:] muestra el ultimo de la lista, [:-1] mustra la lista sin el ultimo

        print(code[::-1])
    return code


def detect_correct_error(code, p):

    n = len(code)

    error_pos = 0

    for i in range(p):

        val = 0

        for j in range(1, n + 1):

            if j & (2 ** i) == (2 ** i):

                val = val ^ int(code[-j])

        error_pos += val * (2 ** i)


    if error_pos:

        print(f"Error found at position: {error_pos}")

        corrected_code = code[:n - error_pos] + str(1 - int(code[n - error_pos])) + code[n - error_pos + 1:]

        return corrected_code

    else:

        print("No error detected.")

        return code


def main():

    original_data = input("Enter the data bits: ")

    m = len(original_data)

    p = calculate_parity_bits(m)



    positioned_data = position_parity_bits(original_data, p)

    hamming_code = calculate_parity_values(positioned_data, p)


    print(f"Hamming Code: {hamming_code}")
    print(p)



    received_code = input("Enter the received Hamming Code: ")

    corrected_code = detect_correct_error(received_code, p)


    print(f"Corrected Hamming Code: {corrected_code}")


if __name__ == "__main__":

    main()