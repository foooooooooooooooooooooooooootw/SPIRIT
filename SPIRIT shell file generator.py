import time


def main():
    current_time = time.strftime("%Y%m%d-%H%M%S")
    filename = input("What's the text file's name?")
    input_file = open(filename, "r+")
    lines = input_file.readlines()
    stripped = [line.strip("\n") for line in lines]

    for i in range(0, len(stripped)):
        stripped[i] = "iptables -A INPUT -s " + stripped[i] + " -j DROP &&"

    compiled = " ".join(str(e) for e in stripped)
    compiled = compiled[:-3]

    output_file = open("{} - compiled IP ban command.sh".format(current_time), "w")
    output_file.write(compiled)
    output_file.close


main()
