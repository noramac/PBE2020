import lcddriver
display = lcddriver.lcd()

def read_str():#llegeix string de 4 linies i dona error si no es valid
    i = 4
    while i > 0:
        line = input()
        if len(line) > 20:
            print('El text no es valid (max 20 caracters per linia)')
            i = 4
            print('Si us plau torna a introduir el text:')
            del total[:]
        else:
            total.append(line)
            i -= 1

def lcd_print():#mostra string de 4 linies a la pantalla
    linex = 1
    for x in total:
        display.lcd_display_string(x, linex)
        linex += 1
    


try:
    display.lcd_clear()
    
    print('Insereix el text que vols que es mostri per pantalla: ')
    print('Ctrl+C per sortir')

    total = []
    read_str()
    lcd_print()
    

except KeyboardInterrupt: # Tanca el programa quan es prem ctrl+c
	print("Adeu!")
	display.lcd_clear()


    
