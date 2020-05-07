#!/usr/bin/env python3

import subprocess
import cmd

class HelloWorld(cmd.Cmd):
    """Simple command processor example."""
    
    def do_shit(self, line):
        print ("HOLY SHIT")
    
    def do_exit(self, line):
        return True

    def do_bitch(self, line):
        print ("SON OF A BITCH")

    def do_fuck(self, line):
        print ("OH MY FUCKING GOD")

    def do_help(self, line):
        print ("Welcome to the FUCK console. All swear words are commands.")

    def do_dick(self, line):
        print ("thinks of sam whittle")

    def do_shit(self, line):
        print ("HOLY SHIT")

if __name__ == '__main__':
    HelloWorld().cmdloop()
