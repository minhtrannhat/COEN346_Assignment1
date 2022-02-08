from lib2to3.refactor import MultiprocessRefactoringTool
from mini_shell import main
from user_info.user_info import get_hostname_from_OS, get_username_from_OS
from threading import Thread
from threads.command_shell_thread import command_shell_thread

class caller(Thread):
    def run(self):
        main_thread = main_shell_thread()
             # capture input from 
        while True:
            command: str = input(
                f"{get_username_from_OS()}@{get_hostname_from_OS()}$ "
            )

            if main_shell_thread.run(command) == -1 :
                break

            
# the interactive shell will execute all commands and quit on 'exit' command
class main_shell_thread:

    def run(self, command) -> int:
        # create, run and wait for command thread to end
        running_command = command_shell_thread(command)
        running_command.start()
        # exit the shell
        if command == "exit":
            return -1
        # we don't join() a background command
        if "&" in command:
            return 0

        running_command.join()
