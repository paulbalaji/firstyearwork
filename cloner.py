import subprocess

if __name__ == "__main__":
    w = open('todo.sh', 'w')
    with open('clone links') as f:
        for line in f:
            command = "git submodule add " + line
            w.write(command)
    w.close()
