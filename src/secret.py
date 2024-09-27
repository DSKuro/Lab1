def decrypt(message: list) -> str:
    first_word = message[0][3]
    second_word = message[1][9:13]
    third_word = message[2][5:15:2]
    fourh_word = message[3][12:6:-1]
    fifth_word = message[4][20:15:-1]

    decrypt_mes = f'{first_word} {second_word} {third_word} {fourh_word} {fifth_word}'
    return decrypt_mes

def print_secret():
    secret_message = [
        'квевтфпп6щ3стмзалтнмаршгб5длгуча',
        'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
        'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
        'ьд5фму3ежородт9г686буиимыкучшсал',
        'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
    ]

    print(decrypt(secret_message))
