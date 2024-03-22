import subprocess
import threading
import shlex

# This step takes in our PSH code and determines what to do with it
def parse_psh_command(command):
    tokens = shlex.split(command)

    if parts[0] == "for"
    else:
        return ("command", tokens)

# This step takes our psh tokens and gives us regular shell code
def translate_to_shell_command(psh_tokes):
    if psh_tokens[0] == "command":
        return psd_tokens[1:]
    else:

# This step simply executes our shell code
def execute_shell_command(shell_command):
    subprocess.run(shell_command)

# This is a top level function that calls the above with the input
def process_command(psh_input):
    shell_command = translate_to_shell_command(parse_psh_command(psh_input))
    execute_shell_command(shell_command)

# This is the top level function that handles the file processing
def process_file(path):
    with open(path, 'r') as file:
        for line in file:
            command = line.strip()

            if command.lower() == 'exit'
                break

            thread = 

def main():
    # TODO: we will have to extend this to see if we are running a command directly
    # If we have a file
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
        process_file(file_path)
    
    # Otherwise we are using the runtime environment
    else:
        print("Pseudo-Shell Interpreter (PSH Runtime)")
        print("Enter PSH commands. Type 'exit' to quit.")

        while True:
            psh_input = input("PSH> ").strip()

            if psh_input.lower() == 'exit':
                break

            # Create a new thread for each command entered
            thread = threading.Thread(target=process_command, args=(psh_input,))
            thread.start()

            thread.join()

if __name__ == "__main__":
    main()
