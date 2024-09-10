#räkna vokaler
def rakna_vokaler(text):
    vokaler = "aeiouåäöAEIOUÅÄÖ"  # Lista på vokaler både små och stora
    # din kod här
antal_vokaler = 0  
   
    for tecken in text:
        if tecken in vokaler:  
            antal_vokaler += 1
   
    return antal_vokaler  

user_input = input("Skriv en bra text: ")

print("Antal vokaler i texten:{} " .format (rakna_vokaler(user_input)))

