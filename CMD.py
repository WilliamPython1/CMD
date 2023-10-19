import subprocess

# The command you want to run in CMD
cmd_command = "dir"  # Replace with your desired CMD command

try:
    # Run the CMD command
    result = subprocess.run(cmd_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)

    # Check if the command was successful (return code 0)
    if result.returncode == 0:
        # Print the output of the command
        print("CMD Output:")
        print(result.stdout)
    else:
        # Print any error message
        print("CMD Error:")
        print(result.stderr)
except Exception as e:
    print("An error occurred:", str(e))
