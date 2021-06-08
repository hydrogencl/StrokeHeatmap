import keyboard
recorded=keyboard.record(until='esc')

file_out = open("./record.txt", "w")

print(len(recorded))
for n in recorded:
    file_out.write("{0:s},{1:d},{2:s},{3:s}\n".format(n.name, n.scan_code, str(n.is_keypad), str(n.modifiers)))
    #print(n, n.scan_code, n.is_keypad)


file_out.close()
